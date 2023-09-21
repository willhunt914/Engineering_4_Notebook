#code credit goes to anton I apreciate his help 
import digitalio
import board
import adafruit_mpu6050 
import busio
import time

sda_pin = board.GP16 ## States the pin for SDA
scl_pin = board.GP17 ## States the pin for SCL
i2c = busio.I2C(scl_pin, sda_pin) ## States the pins for I2C

ledRed = digitalio.DigitalInOut(board.GP1) ## Sets the pin number for the Red LED
ledRed.direction = digitalio.Direction.OUTPUT  

mpu = adafruit_mpu6050.MPU6050(i2c)

while True: 
    XAcceleration = mpu.acceleration[0] ## States which value of the Tuple corresponds to which accelerometer value 
    YAcceleration = mpu.acceleration[1] ## For Y
    ZAcceleration = mpu.acceleration[2] ## For Z

    print(f"XAcceleration = {XAcceleration}") ## Prints the X Accel Value 
    print(f"YAcceleration = {YAcceleration}") ## Prints the Y Accel Value 
    print(f"ZAcceleration = {ZAcceleration}") ## Prints the Z Accel Value 
    print("") ## Adds a space between each reading 
    
    time.sleep(.1) ## Adds a slight pause after each cycle 

    if ZAcceleration < 0:
        ledRed.value = True ## Turns on the Red LED
    else:
        ledRed.value = False ## Turns off the Red LED when the accelerometer is not tilted to exactly 90 degrees