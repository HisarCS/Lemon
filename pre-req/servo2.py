
from time import sleep, ticks_us
import gc
def map_angle(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)


class Servo():
    __current_angle = 90        # the current angle of the servo
    max_angle = 180
    min_angle = 0
    __canLoop=True

    def _us2duty(self, value):
        return int(4095 * value / self.period)

    def __init__(self, i2c, pca9685, address=0x40,freq=50, min_us=600, max_us=2400, degrees=180):
        self.period = 1000000 / freq
        self.min_duty = self._us2duty(min_us)
        self.max_duty = self._us2duty(max_us)
        self.degrees = degrees
        self.freq = freq
        self.pca9685 = pca9685
        self.pca9685.freq(freq)

        



    def show(self):
        print("Pin:", self.pin, "Current Angle:", self.current_angle)
        # print("Pin: ", self.pin)
        # print("Current Angle:", self.current_angle) 

  
    def angle(self, angle_value, channel):
        ''' Sets the angle, in degrees '''
        # print("setting angle for channel", self.channel, "to angle", angle_value)
        if ((angle_value >= 0) and (angle_value > self.min_angle)) and ((angle_value <= 180) and (angle_value <self.max_angle)):
            self.__current_angle = angle_value

            # map values - degrees to duty
            
            duty = map_angle(angle_value, 0, 180, 0, 4096)
            # print("Duty is:", duty, "angle requested is", angle_value)
            # self.__pwm.duty_u16(my_angle)
            self.pca9685.duty(index=channel, value=duty)
            
            sleep(0.0001)
        else:
            print("Angle input is out of bounds(0=< θ =<180), yours:", angle_value)
            __canLoop = False

    def release(self, channel):
        ''' release the break '''
        self.pca9685.duty(channel, 0)
        
    def motion2(self, time, target_angle,delta,channel):
        """
        cura = self.__current_angle
        iteration = self.__change
        if(target_angle<cura):
            sleep(time)
            print(iteration)
            cura = cura + -abs(delta) # this is for minimizing any runtime errors that can be caused when the function is called
            duty = map_angle(cura, 0, 180, 0, 4096)
            self.pca9685.duty(index=channel, value=duty)
            self.__current_angle = cura
            self.__change = iteration + abs(delta)
            
                    
        if(target_angle>cura):                            
            sleep(time)
            print(cura)
            cura = cura + abs(delta)    
            self.__current_angle = cura
            duty = map_angle(cura, 0, 180, 0, 4096)

            self.pca9685.duty(index=channel, value=duty)
            self.__change = iteration + abs(delta)
        
        """
        sleep(0.0000010)
        Lcheck=self.__canLoop
        cura = self.__current_angle
        if ((cura >= 0) and (cura > self.min_angle)) and ((cura <= 180) and (cura <self.max_angle)):       

            iteration=0
            diff=abs(cura-target_angle)
            if(target_angle<cura):
                while(iteration<=diff):

                    sleep(time)
                    print(cura)
                    self.angle(cura,channel)
                    cura = cura - abs(delta) # this is for minimizing any runtime errors that can be caused when the function is called
                    self.__current_angle = cura
                    iteration = iteration + abs(delta)
                    if(Lcheck==False):
                        self.__canLoop = True
                        break
                    
                return
            elif(target_angle>cura):           
                while(iteration<=diff):
                    
                    sleep(time)
                    print(cura)
                    cura = cura + abs(delta)    
                    self.angle(cura,channel)
                    iteration = iteration + abs(delta)
                    if(Lcheck==False):
                        self.__canLoop = True
                        break
#            gc.collect()
                return 
                
    def motion(self, time, target_angle,delta,channel):
        """
        cura = self.__current_angle
        iteration = self.__change
        if(target_angle<cura):
            sleep(time)
            print(iteration)
            cura = cura + -abs(delta) # this is for minimizing any runtime errors that can be caused when the function is called
            duty = map_angle(cura, 0, 180, 0, 4096)
            self.pca9685.duty(index=channel, value=duty)
            self.__current_angle = cura
            self.__change = iteration + abs(delta)
            
                    
        if(target_angle>cura):                            
            sleep(time)
            print(cura)
            cura = cura + abs(delta)    
            self.__current_angle = cura
            duty = map_angle(cura, 0, 180, 0, 4096)

            self.pca9685.duty(index=channel, value=duty)
            self.__change = iteration + abs(delta)
        
        """
        
        Lcheck=self.__canLoop
        cura = self.__current_angle
        if ((cura >= 0) and (cura > self.min_angle)) and ((cura <= 180) and (cura <self.max_angle)):       

            iteration=0
            diff=abs(cura-target_angle)
            if(target_angle<cura):
                while(iteration<=diff):

                    sleep(time)
                    gc.collect()
                    print(cura)
                    self.angle(cura,channel)
                    cura = cura - abs(delta) # this is for minimizing any runtime errors that can be caused when the function is called
                    self.__current_angle = cura
                    iteration = iteration + abs(delta)
                    if(Lcheck==False):
                        self.__canLoop = True
                        break
                    
            elif(target_angle>cura):           
                while(iteration<=diff):
                    
                    sleep(time)
                    gc.collect()
                    print(cura)
                    
                    cura = cura + abs(delta)    
                    self.angle(cura,channel)
                    iteration = iteration + abs(delta)
                    if(Lcheck==False):
                        self.__canLoop = True
                        break
        return
        """              

            
            
            while cura != target_angle:
                if(target_angle <= cura):
                    self.delta = -abs(delta) # this is for minimizing any runtime errors that can be caused when the function is called
                    sleep(time)
                    self.angle(target_angle,channel)
                    if(target_angle != cura):
                        cura = ((target_angle)-(delta))                    
                        self.__current_angle = cura
                        print("if problem")
                elif(target_angle >= cura):
                    self.delta = abs(delta)
                    sleep(time)
                    self.angle(cura,channel)
                    if(target_angle != cura):
                        cura = target_angle + delta
                        self.__current_angle = cura
                        print("if problem")
                print("while problem")
        else:
            print("Angle input is out of bounds(0=< θ =<180), yours:", angle_value)

        """
