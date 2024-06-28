import cv2 as cv
import time 
from PathCreator import PathCreator
from threading import Thread
from Telegram import Telegram
from Detector import Detector
from datetime import datetime

class Camera:
    def __init__(self):
        self.__cameraOn = False
        self.__frame = ""
        self.__width = 1280
        self.__height = 720
        self.__fps = 30
        self.__cam = cv.VideoCapture(0)
        self.__cc = cv.VideoWriter_fourcc(*'mp4v')
        self.__getPath = PathCreator()
        self.__telegram = Telegram()
        self.__detector = Detector()
        self.__isDetectorOn = True
        self.__THREADS = []
        
        self.__THREADS.append(Thread(target=self.startCam))
        self.__THREADS.append(Thread(target=self.__detec))
        for th in self.__THREADS:
            th.daemon = True
            th.start()
            time.sleep(5)
        
   
    def startCam(self):
        print("starting cam")
        while True:
            ret, self.__frame = self.__cam.read()
            cv.putText(self.__frame, str(datetime.now())[:-7], (20, 40), cv.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2, cv.LINE_AA)
            if not ret:
                self.__cameraOn = False
                break
            else: 
                self.__cameraOn = True
        cv.destroyAllWindows()
        
    def __detec(self):
        print("starting detector")
        while True:
            if self.__cameraOn and self.__isDetectorOn:
                if self.__detector.chk_img(self.__frame):
                    path_picture = self.picture()
                    path_video = self.record(30)
                    self.__telegram.sendFile(path_picture, "foto")
                    self.__telegram.sendFile(path_video, "video")
            else:
                pass
            
    def record(self, duration):
        __path = self.__getPath.getPath()
        __file = cv.VideoWriter(__path + ".mp4" , self.__cc, self.__fps, (self.__width, self.__height))
        __startTime = time.time()
        while self.__cameraOn:
            __file.write(self.__frame)
            cv.waitKey(33)
            if time.time() - __startTime >= duration:
                break
        __file.release()
        return __path + ".mp4"

    def picture(self):
        __path = self.__getPath.getPath()
        cv.imwrite(__path + ".jpg" , self.__frame)
        return __path + ".jpg" 
    
    def frame(self):
        try:
            return cv.imencode('.jpeg', self.__frame)[1].tobytes()
        except:
            return b'201'
        
    def turnDetector(self):
        if self.__isDetectorOn:
            self.__isDetectorOn = False 
        else:
            self.__isDetectorOn = True
        
        print(f"Detector: {self.__isDetectorOn}")
        return self.__isDetectorOn
        
