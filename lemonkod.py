#lemonkod.py
# Can Borcbakan, Erem Degerli, IdealabCS
#may 2022

import sys
import time
from time import sleep
from machine import Pin, PWM, UART
import utime

sys.path.insert(0,"/PicoCat-master")

from pca9685 import PCA9685
from machine import I2C
from servo import Servo

# servo 1 ve 30 arasında çalışıyor seb  ebi dişli sayısı (180/6 = 30)


#bluetooth modülü için uart tanımlama
# uart = UART(0,9600)

led = Pin(25, Pin.OUT)
sda=Pin(0)
scl=Pin(1)
id = 0
i2c = I2C(id=id,sda=sda,scl=scl)
print(i2c.scan())
pca = PCA9685(i2c = i2c)

FRF=0
FRT=1
FLF=2
FLT=3
RLF=4
RLT=5
RRF=6
RRT=7

servo = Servo(i2c=i2c,pca9685=pca)
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
    
config()    
sleep(5)
while True:

        servo.motion(0.001,1,0.5,6)

        servo.motion(0.001,1,0.5,7)
  
        servo.motion(0.001,25,0.5,0)

        servo.motion(0.001,25,0.5,1)

        servo.motion(0.001,25,0.5,5)

        servo.motion(0.001,1,0.5,6)

        servo.motion(0.001,1,0.5,2)

        servo.motion(0.001,1,0.5,3)




        servo.motion(0.001,25,0.5,2)

        servo.motion(0.001,25,0.5,3)

        servo.motion(0.001,1,0.5,5)

        servo.motion(0.001,1,0.5,5)

        servo.motion(0.001,1,0.5,6)

        servo.motion(0.001,25,0.5,7)

        servo.motion(0.001,25,0.5,0)

        servo.motion(0.001,25,0.5,1)
"""
i = 120

config()

sleep(2)

servo.release(0)
servo.release(1)
servo.release(2)
servo.release(3)
servo.release(12)
servo.release(13)
servo.release(14)
servo.release(15)
#servo.release(1,2)
#sleep(2)

for i in range(1,180,1):
    sleep(0.1)
    servo.angle(i,1)
    servo.angle(i,3)

servo.release(0)
servo.release(2)

while True:
    if uart.any():
        command = uart.readline() 				#geri gelen sinyali command diye tanımladık
        command.alllowercase() 					# bu çalışmayacak, doğru kod'a bakmak lazım
        while(command=="walk"): 				#yürüme komutunu walk diye tanımladık
            distance = dist()                   #and komutu ile 2 kodu birsden çalıştır
#başlangıç ve başlangıça dönüşü iflerle tasarla, artış ve azalış ilk değere kadar gitmesini engelliyor 
            while(distance>5):
"""
