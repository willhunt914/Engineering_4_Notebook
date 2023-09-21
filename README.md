# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)
* [LED_countdown](#LED_countdown)
* [LED_Blink](#LED_Blink)
* [LED_Button](#LED_Button)
* [LED_Servo](#LED_Servo)

&nbsp;

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!



## LED_countdown

In this assignment, the goal was to print a countdown from 10 onto the serial monitor. 

### Evidence 

https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/af838a00-3ca4-4e31-a20d-81ef6e5d72cf


### Code

[Launchpad code](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad1.py) 

### Reflection


I learned that if you want to code a countdown you  put  the desired range within parentheses, separated by a comma, with the final number indicating the step size for counting down or up. You also have to import time, board, digitalio, and sleep to make the code work.








### LED_Blink

The goal of this assignment was to add on to the previous code and have an LED blink red during the countdown and blink green during the liftoff 


### Evidence 

https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/0c899f61-b17b-4c13-8bcb-3787726edbf5



### Wiring

![image](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/b969c414-eb78-4470-a33c-474caac397ea)

### Code
[Launchpad2](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad2.py)

### Reflection

The only thing that I had to figure out was how to set the red and green LEDs to the correct pins. I learned that you can hit Ctrl + Shift + P to open the pin map since the pico does not have labeled pins. 



## LED_Button

The goal of this assignment was to add a button to start the countdown.

### Evidence 

https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/14392a1c-eeb7-4211-9470-7910a84a03cc

### Wiring

![launchpad button](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/93706350-1e56-4929-9789-5ebe6b948c03)

### Code
[Launchpad3](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad3.py)

### Reflection


In the code for LEDs, I discovered that you need to set the direction as OUTPUT, while for buttons, it should be set as INPUT. I learned that  sleep() causes the code to pause for a desired amount of time. The digitalio.Pull.UP" line lets the button use its internal resistor.




## LED_Servo

The goal of this assignment was to make a servo sweep to 180 degrees at the end of the countdown.

### Evidence 


https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/8132c0a0-9ae0-4c5d-840c-dac946df110b


### Wiring

![image](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/8793d51f-b98d-401c-ae42-a05d62c7ce7a)


### Code
[Launchpad4](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad4.py)

### Reflection


This was one of the easiest assignments for me. If you want the servo to work you have to download the adafruit_moter library. You should also have code before your "while true" that resets the servo angle to 0 every time you run the code.


## Crash_Avoidance1

The goal of this assignment was to have an accelerometer display the x, y, and z values on the serial monitor.
### Evidence 

https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/5421a727-4bcc-4d8f-ba93-e6f4d3e3ab7b

### Wiring

![accelerometer](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/e0924352-b7ff-47cf-aeeb-231e19e2afbd)


### Code
[accel1code](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/CrashAvoidance1.py)

### Reflection

To get this code to work you have to import the adafruit_mpu6050.mpy, adafruit_bus_device, and the  adafruit_register folders. The sleep(delay) gives the sensor a more accurate reading. Having a .1 second delay between readings is a  good time.















&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;






