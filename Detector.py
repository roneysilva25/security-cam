import imutils
import cv2 as cv

class Detector:
    def __init__(self):
        self.start_frame = ""
        self.__first_time = True
    
    def chk_img(self, frame):
        if self.__first_time:
            self.start_frame = imutils.resize(frame, width=500)
            self.start_frame = cv.cvtColor(self.start_frame, cv.COLOR_BGR2GRAY)
            self.start_frame = cv.GaussianBlur(self.start_frame, (21, 21), 0)
            self.__first_time = False
        else: 
            frame = imutils.resize(frame, width=500)
            frame_bw = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frame_bw = cv.GaussianBlur(frame_bw, (5, 5), 0)
            
            difference = cv.absdiff(frame_bw, self.start_frame)
            threshold = cv.threshold(difference, 25, 255, cv.THRESH_BINARY)[1]
            self.start_frame = frame_bw 
            
            if threshold.sum() > 1000:
                return True
        