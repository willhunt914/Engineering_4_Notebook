# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)
* [LED_countdown](#LED_countdown)
* [LED_Blink](#LED_Blink)
* [LED_Button](#LED_Button)
* [LED_Servo](#LED_Servo)
* [Crash_Avoidance1](#Crash_Avoidance1)
* [Crash_Avoidance2](#Crash_Avoidance2)
* [Crash_Avoidance3](#Crash_Avoidance3)
* [Area_Finder](#Area_Finder)
* [Area_Finder2](#Area_Finder2)
* [Morsecode1](#Morsecode1)
* [Morsecode2](#Morsecode2)
* [DataSaver1](#DataSaver1)
* [DataSaver2](#DataSaver2)
* [Beam_Designpt1](#Beam_Designpt1)
* [Beam_Simulation](#Beam_Simulation)
* [Beam_Fixing](#Beam_Fixing)
&nbsp;


Credit for most of these assignments goes to Afton in case I forgot to write it. 

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
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 

### Evidence 

https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/af838a00-3ca4-4e31-a20d-81ef6e5d72cf


### Code

[Launchpad code](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad1.py) 

### Reflection


I learned that if you want to code a countdown you  put  the desired range within parentheses, separated by a comma, with the final number indicating the step size for counting down or up. You also have to import time, board, digitalio, and sleep to make the code work.








### LED_Blink

The goal of this assignment was to add on to the previous code and have an LED blink red during the countdown and blink green during the liftoff 
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 


### Evidence 

https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/0c899f61-b17b-4c13-8bcb-3787726edbf5



### Wiring

![image](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/b969c414-eb78-4470-a33c-474caac397ea)

### Code
[Launchpad2](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/launchpad2.py)

### Reflection

The only thing that I had to figure out was how to set the red and green LEDs to the correct pins. I learned that you can hit Ctrl + Shift + P to open the pin map since the pico does not have labeled pins. 



## LED_Button
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 

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
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 

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
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 

The goal of this assignment was to have an accelerometer display the x, y, and z values on the serial monitor.
### Evidence 

https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/5421a727-4bcc-4d8f-ba93-e6f4d3e3ab7b

### Wiring

![accelerometer](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/e0924352-b7ff-47cf-aeeb-231e19e2afbd)


### Code
[crash avoidence 1 code](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/CrashAvoidance1.py)

### Reflection

To get this code to work you have to import the adafruit_mpu6050.mpy, adafruit_bus_device, and the  adafruit_register folders. The sleep(delay) gives the sensor a more accurate reading. Having a .1 second delay between readings is a  good time.


## Crash_Avoidance2
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 

The goal of his assignment was to make an LED Blink if the Pico was tilted more than 90 degrees. We also had to add a battery pack to the board so that it could be powered without the computer.
### Evidence 


https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/694696e7-bb4a-4e17-a20b-097bbb35f933


### Wiring

![crash2](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/104b04c9-929c-4a0e-b3db-ffc2e515c893)


### Code
[crash avoidence 2 code](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/crash2.py)

### Reflection


The main problem I had was trying to figure out how to get the battery to work. I learned that you have to charge your battery for it to work. I learned that the longer side of the LED goes to positive. 



## Crash_Avoidance3
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 

The goal of this assignment was to have an OLED that displays the x, y, and z values rounded to the nearest 3 decimal places.

### Evidence 


https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/6c8088b4-d02c-4d67-95a8-7a546e6caee4


### Wiring
![crash3](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/c36fbbb0-88d5-4fb2-a073-72e0f22d8ecb)



### Code
[crash avoidence 3 code](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/crash3.py)

### Reflection



Again, I had more problems with the wiring. I often flipped the SCL and SDA pins which caused my code to not work. I also didnt read the assignment and forgot to download the libraries so after I downloaded them it worked first try. 

## Area_Finder 

The goal of this assignment is to have the code ask for three X and Y coordinates and for it to pop out the area. 
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 


### Evidence 


https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/ddbc047a-5202-4af1-b019-cfaa75cc0842


### Code 

[AreaCode](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/area.py)

### Reflection

The main trouble I had was figuring out how to do functions. With a little help from Afton, I learned that the try-except command is used to make sure that the user inputs the coordinates in the right way. This code also runs in an infinite loop so you don't have to run it every single time. 


## Area_Finder2 

 the goal of this assignment is to have an onboard OLED screen that plots each triangle on a graph relative to the base location.
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 


### Evidence 

https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/9856d122-5dbd-4f9d-9c5d-68cf3ba4f9c1


### Code 

[Area2Code](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/area2.py)
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 


### Wiring

![area 2 wiring](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/d16c93d3-9b37-4f14-a3ed-f078cf30a664)

### Reflection

Again, I had trouble with wiring up the OLED screen. I figured out that the Clk wires up to Scl and that SDA wires up to date. My code was not working because It was in  a file named Code.py and not the actual folder so I learned to not do that. 


## Morsecode1

 The goal of this assignment was to have code that translates words into morris code 
 Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 


### Evidence 


https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/d5b514b1-e7c4-4c2c-99f6-b486ab7921aa


### Code 

[morse1Code](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/morsecode.py)


### Reflection

I learned that the .upper() line lets the code work in upper and lowercase. The code uses the try-except line to make sure that special characters that will break the code don't work. For each letter the code looks in the MORSE_CODE library and translates it to Morse code. 


## Morsecode2

The goal was to have an LED blink the message that you type in Morse code. 
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 


### Evidence 

https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/3e1ee0ff-3bbd-44ba-9ba1-8ea0e2a94fca

### Wiring

![mnorsecode2](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/eeda6263-f1c0-4fb0-8d20-bb67d2306ddb)

### Code 

[morse2code](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/morsecode2.py)

### Reflection

I had trouble putting the LED in the right direction. To fix this Afton showed me that the longer side connects to the PICO and the shorter side goes into the negative side on the breadboard. I learned that the code uses certain delays for each character.

## DataSaver1

The goal of this assignment was to have data saved on the PICO when it is unplugged and then put the data in a file when it is plugged in. 
Credit for this code goes to [Afton](https://github.com/Avanhoo/Engineering_4_Notebook) 


### Evidence 


https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/ab08535c-0301-46c7-a7e6-e8f99e3fa65e

[data.csv](https://github.com/willhunt914/Engineering_4_Notebook/files/13366272/data.csv)


### Wiring

![datasaver](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/4d444e3e-a403-4f04-b008-f0cb87ab0d42)

### Code

[data1code](https://github.com/willhunt914/Engineering_4_Notebook/blob/main/raspberry-pi/data1.py)

### Reflection

The main problem I had was not reading the assignment all the way. I didn't make a boot.py so my code was not working. The wiring of my accelerometer was also off by one row so I had to fix that. 

## DataSaver2

The goal of this assignment was to graph our data 

### Evidence 

![acceleration values](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/4182852e-7a2f-4941-961c-929f80bea855)


[Link to spreadsheet](https://docs.google.com/spreadsheets/d/1bCEzuUYCmRRxUKbU-nJmMzW54dc3cUvWYF7U1CbMroA/edit#gid=0)

### Reflection

This assignment was really easy since it showed us how to do everything. The only problem was that I didn't read it and struggled with how to add an X-axis. I learned you click the window and select the x-axis data you want. 




















## Beam_Designpt1

The goal of this assignment is to design a beam to hold as much weight as possible. For the beam to fail it must either break or bend more than 35mm.

### Part Link 

[link to Onshape document](https://cvilleschools.onshape.com/documents/36bd5e50c7a6146a0cebf6d6/w/d8e6fba93b7971cd2c68e99e/e/df01e9a616645a5b4969e98e?renderMode=0&uiState=651d665b66bcfe34cbaa237b). 

### Part Image

![Screenshot 2023-10-04 094221](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/ce85f07b-a939-41c9-9d8b-80b9c6b16c88)

### Reflection

![Screenshot 2023-10-02 103925](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/be683c92-1139-4a28-bc43-c720530f2ead)

In our first design shown above, the main problem we ran into was overhang. Overhang is when the printer does not have any surface to print onto. To fix this, we had to add supports at 45 degrees under the overhang shown below:

![overhang fix](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/918b776b-4988-4ba2-9ccc-fd73b1ada283)

Additionally, the project was breaching the weight limit so we added a lot of fillets to reconcile that.


## Beam_Simulation

The goal of this assignment is to run a simulation in Onshape to find the weak points of the beam

### Part Link 

[link to Onshape document](https://cvilleschools.onshape.com/documents/36bd5e50c7a6146a0cebf6d6/w/d8e6fba93b7971cd2c68e99e/e/df01e9a616645a5b4969e98e?renderMode=0&uiState=651d665b66bcfe34cbaa237b). 

### Part Image
![unnamed](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/ec073d91-6b3a-4ec3-a803-6408e5517261)

Displacement Plot

![We live in a simulation](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/9419c4c3-0af8-4bd8-9a25-76607ef6002a)

Stress Plot 
### Reflection

The side closer to the holder faces the most stress and the side away from it faces almost none. To fix this, we will remove some of the weight on the other side so that we can add more structure to the weaker side.



## Beam_Fixing

The goal of this assignment was to use the information from the simulation to design a better beam.

### Part Link 

[link to Onshape document](https://cvilleschools.onshape.com/documents/36bd5e50c7a6146a0cebf6d6/w/d8e6fba93b7971cd2c68e99e/e/df01e9a616645a5b4969e98e?renderMode=0&uiState=651d665b66bcfe34cbaa237b). 

### Part Image
![FIXEDBEAM](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/8381824b-0b3a-4ff1-8303-b71e8b79694c)


Stress Plot 
### Reflection

To fix the problems we had we added a piece that would support the beam underneath the holder. 

![fixything](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/eb4a3234-b0af-4ad6-af5d-e8657807711e)

We also thickened the part shown below that was thin and weak in our first design. 

![Screenshot 2023-10-11 092815](https://github.com/willhunt914/Engineering_4_Notebook/assets/71402974/31c1bad6-2b97-4eaa-bac3-eec7c41a23f0)

To keep the weight under 13 grams we added more fillets to the stronger side of the beam. Before the changes, the maximum displacement was 65.51 and the max stress was 10,025 psi. After the changes the displacement got slightly worse to 71.59 but the max stress it could take went up to 16,340.

















&nbsp;










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







