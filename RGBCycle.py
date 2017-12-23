import RPi.GPIO as GPIO
from time import sleep
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red = 5
green = 13
blue = 19
anode = 6
button = 26 #USING PUSHBUTTON TO CANCEL THE PROGRAM

GPIO.setup(anode, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

GPIO.output(anode, 1)

while not GPIO.input(26):
	#RED
	GPIO.output(blue, 1)
	GPIO.output(red, 0)
	GPIO.output(green, 1)
	sleep(0.5)
	#GREEN    
	GPIO.output(blue, 1)
	GPIO.output(red, 1)
	GPIO.output(green, 0)
	sleep(0.5)
	#BLUE
	GPIO.output(blue, 0)
	GPIO.output(red, 1)
	GPIO.output(green, 1)
	sleep(0.5)
	#RANDOM RGB COLOR
	GPIO.output(blue, randint(0,1))
	GPIO.output(red, randint(0,1))
	GPIO.output(green, randint(0,1))
	sleep(1)
    
GPIO.cleanup()
