
import time
import board
import digitalio
from time import sleep

#thank you very much afton for the help with this credit goes to him 

redled = digitalio.DigitalInOut(board.GP0) #sets pin for red led 
redled.direction = digitalio.Direction.OUTPUT

greenled = digitalio.DigitalInOut(board.GP1) #sets pin for green led 
greenled.direction = digitalio.Direction.OUTPUT


Button = digitalio.DigitalInOut(board.GP16) #sets pin for red led 
Button.direction = digitalio.Direction.INPUT


if  Button.value == False: 
    for i in range (10,0,-1): #starts from 10 and counts down to 0
        print(i)
        redled.value = True #turns red led on 
        sleep(1)
        redled.value = False #turns red led off
        sleep(.5)
    print("liftoff")
    greenled.value = True #turn green led on 
    sleep(1)
