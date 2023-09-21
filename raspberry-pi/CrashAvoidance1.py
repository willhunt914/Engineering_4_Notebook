#thank you very much afton for the help with this credit goes to him 
import board
import busio
import adafruit_mpu6050
from time import sleep
#imports libraries


sda_pin = board.GP16
scl_pin = board.GP17
#tells what pins to use

i2c = busio.I2C(scl_pin, sda_pin)
imu = adafruit_mpu6050.MPU6050(i2c)
x = 0
y = 0
z = 0


#defines delay
delay = .1

sleep(delay)

while True:
    print(f"Accel: {round(imu.acceleration[0]-.6,1)}, {round(imu.acceleration[1]+.2,1)}, {round(imu.acceleration[2],1)}")  #print accelerometer values 
    sleep(delay) #sleep for set delay before next print

