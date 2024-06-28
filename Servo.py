import RPi.GPIO as GPIO
from time import sleep

class Servo():
    def __init__(self):
        self.__step = 1
        self.__duty = 7
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        self.__servo1 = GPIO.PWM(11, 50)
        self.__servo1.start(0)
        
    def __servo(self, duty):
        self.__servo1.ChangeDutyCycle(duty)
        sleep(0.1)
        self.__servo1.ChangeDutyCycle(0)
    
    def left(self):
        if self.__duty >= 2:
            self.__duty -= 0.5
            self.__servo(self.__duty)
  
    
    def right(self):
        if self.__duty <=7:
            self.__duty += 0.5
            self.__servo(self.__duty)
  
    
    def center(self):
        self.__duty = 7
        self.__servo(self.duty)