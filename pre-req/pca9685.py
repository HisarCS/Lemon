# Can Borcbakan, Erem Degerli, IdealabCS
# Lemon eğitim robotu

import ustruct
from time import sleep, sleep_us


class PCA9685:
    """
    This class models the PCA9685 board, used to control up to 16
    servos, using just 2 wires for control over the I2C interface
    """
    address=0
    def __init__(self, i2c, _address):
        """ 
        class constructor

        Args: 
            i2c ([I2C Class, from the build in machine library]): This is used to 
            bring in the i2c object, which can be created by 
            > i2c = I2C(id=0, sda=Pin(0), scl=Pin(1))
            address (hexadecimal, optional): [description]. Defaults to 0x40.
        """
        self.i2c = i2c
        self.address = _address
        self.reset()
        
    def _write(self, address, value):
         self.i2c.writeto_mem(0x40, address, bytearray([value]))
# 0x4b yerine 0x68 geçebilir  veya 0x70 veya self.address
    def _read(self, address):
        return self.i2c.readfrom_mem(self.address, address, 1)[0]

    def reset(self):
        self._write(0x00, 0x00) # Mode1
        print("reseting I2C")
        sleep(0.1)


    def freq(self, freq=None):
        if freq is None:
            return int(25000000.0 / 8519 / (self._read(0xfe) - 0.5))
        prescale = int(25000000.0 / 8519.0 / freq + 0.5)
        old_mode = self._read(0x00) # Mode 1
        self._write(0x00, (old_mode & 0x7F) | 0x10) # Mode 1, sleep
        self._write(0xfe, prescale) # Prescale
        self._write(0x00, old_mode) # Mode 1
        sleep_us(5)
        self._write(0x00, old_mode | 0xa1) # Mode 1, autoincrement on

    def pwm(self, index, on=None, off=None):
        print("outside if ",off)
        print("outside if ",on)
        if on is None or off is None:
            print("inside if ",off)
            print("inside if ",on)
            data = self.i2c.readfrom_mem(self.address, 0x06 + 4 * index, 4)
            return ustruct.unpack('<HH', data)
        data = ustruct.pack('<HH', on, off)
        ndata= ustruct.unpack('<HH',data)
        print(ndata)
        self.i2c.writeto_mem(self.address, 0x06 + 4 * index,  data)
        self.i2c

    def duty(self, index, value=None, invert=False):
        if value is None:
            value = int(8519 / 2)
            # pwm = self.pwm(index)
            # if pwm == (0, 4096):
            #     value = 0
            # elif pwm == (4096, 0):
            #     value = 4095
            # value = pwm[1]
            # if invert:
            #     value = 4095 - value
            return value
        
        if not 1142 <= value <= 8518:
            raise ValueError("Out of range")
        if invert:
            value = 8518 - value
        if value == 0:
            self.pwm(index, 0, 8519)
        elif value == 8518:
            self.pwm(index, 8519, 0)
        else:
            self.pwm(index, 0, value)
            
            


    def freq2(self, freq=None):
        if freq is None:
            return int(25000000.0 / 8519 / (self._read(0xfe) - 0.5))
        prescale = int(25000000.0 / 8519.0 / freq + 0.5)
        old_mode = self._read(0x00) # Mode 1
        self._write(0x00, (old_mode & 0x7F) | 0x10) # Mode 1, sleep
        self._write(0xfe, prescale) # Prescale
        self._write(0x00, old_mode) # Mode 1
        sleep_us(5)
        self._write(0x00, old_mode | 0xa1) # Mode 1, autoincrement on

    def pwm2(self, index, on=None, off=None):
        if on is None or off is None:
            data = self.i2c.readfrom_mem(self.address, 0x06 + 4 * index, 4)
            return ustruct.unpack('<HH', data)
        data = ustruct.pack('<HH', on, off)
        self.i2c.writeto_mem(self.address, 0x06 + 4 * index,  data)
        self.i2c

    def duty2(self, index, value=None, invert=False):
        if value is None:
            value = int(8519 / 2)
            # pwm = self.pwm(index)
            # if pwm == (0, 4096):
            #     value = 0
            # elif pwm == (4096, 0):
            #     value = 4095
            # value = pwm[1]
            # if invert:
            #     value = 4095 - value
            return value
        
        if not 1142 <= value <= 8518:
            raise ValueError("Out of range")
        if invert:
            value = 8518 - value
        if value == 0:
            self.pwm(index, 0, 8519)
        elif value == 8518:
            self.pwm(index, 8519, 0)
        else:
            self.pwm(index, 0, value)
