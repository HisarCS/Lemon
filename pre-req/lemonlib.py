import sys
import time
from time import sleep
from machine import Pin, PWM, UART
import utime


sys.path.insert(0,"/PicoCat-master")

from pca9685 import PCA9685
from machine import I2C
from servo import Servo




class LemonCore():
    def __init__(self):
        sda=Pin(0)
        scl=Pin(1)
        id = 0
        i2c = I2C(id=id,sda=sda,scl=scl)
        print(i2c.scan())
        pca = PCA9685(i2c = i2c)
        servo = Servo(i2c=i2c,pca9685=pca)
        
        FRF=0
        FRT=1
        FLF=2
        FLT=3
        RLF=4
        RLT=5
        RRF=6
        RRT=7

        #çift pinler femur, tek pinler tibia
        def config():
            servo.angle(15,FRF)
            servo.angle(13,FLF)
            servo.angle(13,RLF)
            servo.angle(12,RRF)
            servo.angle(21,FRT)
            servo.angle(8,FLT)
            servo.angle(15,RRT)
            servo.angle(1,RLT)  
            
        def calibF():
            servo.angle(15,FRF)
            servo.angle(13,FLF)
            servo.angle(13,RLF)
            servo.angle(12,RRF)
         

        def calibT():
            servo.angle(1,FRT)
            servo.angle(179,FLT)
            servo.angle(179,RRT)
            servo.angle(1,RLT)
            
        def greeting():
            config()
            servo.motion(0.1,1,1,FLF)
            servo.motion(0.1,7.5,1,FLT)
            servo.motion(0.1,8,1,FLT)
            servo.motion(0.1,7.5,1,FLT)
        def stop():
            servo.release(FRF)
            servo.release(FLF)
            servo.release(RLF)
            servo.release(RRF)
            servo.release(FRT)
            servo.release(FLT)
            servo.release(RRT)
            servo.release(RLT)  
        

class Ultrasonic(LemonCore):
    trigger=None
    echo=None

    def __init__(self,pin_a,pin_b):
        self.trigger=pin_a
        self.echo=pin_b
    
    #ultrason pin tanımlama


    #ultrason ile mesafe ölçme kodu
    def dist(self):
       trigger.low()
       utime.sleep_us(2)
       trigger.high()
       utime.sleep_us(5)
       trigger.low()
       while echo.value() == 0:
           off = utime.ticks_us()
       while echo.value() == 1:
           on = utime.ticks_us()
       timepassed = on - off
       distance = (timepassed * 0.0343) / 2
       return distance

