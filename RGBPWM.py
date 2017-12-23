import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red = 5
green = 13
blue = 19
anode = 6
button = 26 #USING PUSHBUTTON TO CANCEL THE PROGRAM

GPIO.setup(anode, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

GPIO.output(anode, 1)

Freq = 100

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)

#START WITH RED
RED.start(1)
GREEN.start(100)
BLUE.start(100)
        
while not GPIO.input(26):
		#RED TO GREEN
        for x in range(1,101):
                GREEN.ChangeDutyCycle(101-x)
                RED.ChangeDutyCycle(x)
                sleep(0.05)
		#GREEN TO BLUE
        for x in range(1,101):
                GREEN.ChangeDutyCycle(x)
                BLUE.ChangeDutyCycle(101-x)
                sleep(0.05)
		#BLUE TO RED
        for x in range(1,101):
                RED.ChangeDutyCycle(101-x)
                BLUE.ChangeDutyCycle(x)
                sleep(0.05)

GPIO.cleanup()
