# Can Borcbakan, Erem Degerli, IdealabCS
# Lemon eğitim robotu

import sys
import time
from time import sleep
from machine import Pin, PWM, UART
import utime

sys.path.insert(0,"/pre-req")

from pca9685 import PCA9685
from machine import I2C
from servo2 import Servo
import _thread



#i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
#imu = MPU6050(i2c)
# servo 1 ve 30 arasında çalışıyor seb  ebi dişli sayısı (180/6 = 30)


#bluetooth modülü için uart tanımlama
# uart = UART(0,9600)
    
led = Pin(25, Pin.OUT)
sda=Pin(0)
scl=Pin(1)
id = 0
i2c = I2C(id=id,sda=sda,scl=scl)
print(i2c.scan())
pca = PCA9685(i2c = i2c, _address = 0x40)
#Assigning the servo channel values for the PCA9685

FRF=0
FRT=15
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
    servo.angle(15,FLF)
    servo.angle(15,RLF)
    servo.angle(10,RRF)
    servo.angle(5,FRT)
    servo.angle(9,FLT)
    servo.angle(11,RRT)
    servo.angle(9,RLT)

def calib():

    servo.angle(15,FRF)
    servo.angle(15,FLF)
    servo.angle(16,RLF)
    servo.angle(12,RRF)

    servo.angle(10,FRT)
    servo.angle(16,FLT)
    servo.angle(9,RRT)
    servo.angle(13,RLT)    
    
def calibF():
    servo.angle(15,FRF)
    servo.angle(13,FLF)
    servo.angle(13,RLF)
    servo.angle(12,RRF)
 

def calibT():
    servo.angle(1,FRT)
    servo.angle(30,FLT)
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
"""
def stand():
    stop()
    sleep(1)
    servo.angle(9,RRF)
    servo.angle(18,RLF)
    servo.angle(15,FRF)
    servo.angle(15,FLF)
#    servo.angle(20,FLT)
    sleep(0.5)
    thread0 = _thread.start_new_thread(servo.motion, (0.1,12,0.1,RLT))
    sleep(0.1)
    servo.motion(0.1,9,0.1,RRT)
    sleep(0.1)
    servo.motion(0.1,8,0.1,RLT)
    sleep(0.1)
    servo.motion(0.1,8.9,0.1,RRT)
    sleep(0.1)
    servo.motion(0.1,5,0.1,FRT)
    sleep(0.1)
    servo.motion(0.1,9,0.1,FLT)
    sleep(0.1)
    servo.angle(11,RRT)
    servo.angle(9,RLT)
"""
def stand():
    stop()
    sleep(1)
    servo.angle(9,RRF)
    servo.angle(18,RLF)
    servo.angle(15,FRF)
    servo.angle(15,FLF)
#    servo.angle(20,FLT)
    sleep(0.5)

    thread0 = _thread.start_new_thread(servo.motion,(0.1,8,0.1,RLT))
    servo.motion(0.1,8.9,0.1,RRT)
    sleep(0.1)
    thread0 = _thread.start_new_thread(servo.motion,(0.1,5,0.1,FRT))
    servo.motion(0.1,9,0.1,FLT)
    sleep(0.1)
    servo.angle(11,RRT)
    servo.angle(9,RLT)
def start():
    servo.angle(15,FRF)
    servo.angle(15,FLF)
    servo.angle(15,RLF)
    servo.angle(15,RRF)

    servo.angle(15,FRT)
    servo.angle(15,FLT)
    servo.angle(15,RRT)
    servo.angle(15,RLT)

servo.angle(15,FLF)
servo.angle(16,FLT)
sleep(1)
while True:
    thread0 = _thread.start_new_thread(servo.motion2, (0.1,12,0.1,FLF))
    servo.motion(0.1,9,0.1,FLT)
    sleep(1)
    thread1 = _thread.start_new_thread(servo.motion2, (0.1,9,0.1,FLF))
    servo.motion(0.1,12,0.1,FLT)    
    
"""
start()
sleep(0.5)
servo.motion(0.1,5,0.5,RRT)
sleep(1)
calib()
sleep(0.5)
stand()


while True:
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)


#yapılması gerekilenler:
#gyro hız bağlantısı
#femur ve tibialardaki hareket miktarını eşitlemek
# femur için 12-18 aralığı (FRF'ye göre seçtim) yeterli duruyor

def walk():
    count =0
    while True:
    #    gx=round(imu.gyro.x)
     #   gy=round(imu.gyro.y)
     #   gz=round(imu.gyro.z)
        if(count==0):
            posFRF=15
            posFRT=5
            posFLF=1
            posFLT=9
            posRLF=15
            posRLT=9
            posRRF=10
            posRRT=9.5
            count = 1
        else:
            inc=5
            dec=20
            posFRF=20
            posFRT=20
            posFLF=5
            posFLT=5
            posRLF=5
            posRLT=20
            posRRF=5
            posRRT=20
        while (posFRF>=5) and (posFRT>=5) and (posFLF<=20) and (posFLT<=20) and (posRLF<=20) and (posRLT>=5) and (posRRF<=20) and (posRRT>=5):

            servo.angle(posRRF,RRF)
            sleep(time)
            servo.angle(posRRT,RRT)
            sleep(time)
            servo.angle(posFRF,FRF)
            sleep(time)
            servo.angle(posFRT,FRT)
            sleep(time)
            servo.angle(posRLT,RLT)
            sleep(time)
            servo.angle(posRLF,RLF)
            sleep(time)
            servo.angle(posFLF,FLF)
            sleep(time)
            servo.angle(posFLT,FLT)
            sleep(time)
            posFRF= posFRF - 0.5
            posFRT= posFRT - 0.5
            posFLF= posFLF + 0.5
            posFLT= posFLT + 0.5
            posRLF= posRLF + 0.5
            posRLT= posRLT - 0.5
            posRRF= posRRF + 0.5
            posRRT= posRRT - 0.5


        posFRF=5
        posFRT=5 
        posFLF=20
        posFLT=20
        posRLF=20
        posRLT=5
        posRRF=20
        posRRT=5
        while (posFRF<=20) and (posFRT<=20) and (posFLF>=5) and (posFLT>=5) and (posRLF>=5) and (posRLT<=20) and (posRRF>=5) and (posRRT<=20):
            servo.angle(posFLF,FLF)
            sleep(time)
            servo.angle(posFLT,FLT)
            sleep(time)
            servo.angle(posRLF,RLF)
            sleep(time)
            servo.angle(posRLT,RLT)
            sleep(time)
            servo.angle(posRRF,RRF)
            sleep(time)
            servo.angle(posRRT,RRT)
            sleep(time)
            servo.angle(posFRF,FRF)
            sleep(time)
            servo.angle(posRRT,FRT)
            sleep(time)
            posFRF= posFRF + 0.5
            posFRT= posFRT + 0.5
            posFLF= posFLF - 0.5
            posFLT= posFLT - 0.5
            posRLF= posRLF - 0.5
            posRLT= posRLT + 0.5
            posRRF= posRRF - 0.5
            posRRT= posRRT + 0.5

time = 0.1
delta =0.1
config()
sleep(2)
servo.angle(5,0)
stop()
walk()

while True:
    if uart.any():
        command = uart.readline() 				#geri gelen sinyali command diye tanımladık
        command.alllowercase() 					# bu çalışmayacak, doğru kod'a bakmak lazım
        while(command=="walk"): 				#yürüme komutunu walk diye tanımladık
            distance = dist()                   #and komutu ile 2 kodu birsden çalıştır
#başlangıç ve başlangıça dönüşü iflerle tasarla, artış ve azalış ilk değere kadar gitmesini engelliyor 
            while(distance>5):
"""