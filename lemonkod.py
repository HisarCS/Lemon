import sys
import time
from machine import Pin, PWM, UART
import utime

sys.path.insert(0,"/PicoCat-master")

from pca9685 import PCA9685
from machine import PWM, Pin, I2C
from servo import Servo


led = Pin(25, Pin.OUT)
sda=Pin(0)
scl=Pin(1)
id = 0
i2c = I2C(id=id,sda=sda,scl=scl)
# devices = i2c.scan()

"""for d in devices:
    print(hex(d))
    utime.sleep(1)
    """
pca = PCA9685(i2c = i2c)


def velocity(speed):
    
    
