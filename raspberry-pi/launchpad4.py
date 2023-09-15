#thank you very much afton for the help with this credit goes to him 
import time
import board
import digitalio
from time import sleep
import pwmio
from adafruit_motor import servo
pwm_servo = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

redled = digitalio.DigitalInOut(board.GP0) #sets pin for red led 
redled.direction = digitalio.Direction.OUTPUT

greenled = digitalio.DigitalInOut(board.GP1) #sets pin for green led 
greenled.direction = digitalio.Direction.OUTPUT


Button = digitalio.DigitalInOut(board.GP16) #sets pin for Button
Button.direction = digitalio.Direction.INPUT
Button.pull = digitalio.Pull.UP #internally resists the button aparently 

servo.angle = 0

while True:
    if Button.value == False: 
        for i in range (10,0,-1): #starts from 10 and counts down to 0
            print(i)
            redled.value = True #turns red led on 
            sleep(0.25)
            redled.value = False #turns red led off 
            sleep(0.25)
        print("liftoff")
        greenled.value = True #turn green led on 
        sleep(1)
        servo.angle = 180
        sleep(1)
