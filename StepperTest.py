#DRV8825
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

DIR = 20 #PIN20 - DIRECTION
STEP = 21 #PIN21 - STEP
CW = 1 #ROTATION CLOCKWISE
CCW = 0 #ROTATION COUNTERCLOCKWISE
SPR = 200 # STEPS PER REVOLUTION (360 / 1.8) NEMA 17


GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.output(DIR,CW)

step_count = SPR
delay = .005 #step delay (1s/200)

for x in range(step_count):
  GPIO.output(STEP, GPIO.HIGH)
  sleep(delay)
  GPIO.output(STEP, GPIO.LOW)
  sleep(delay)

sleep(5)
GPIO.output(DIR,CCW) #switch rotation to CCW and do loop
for x in range(step_count):
  GPIO.output(STEP, GPIO.HIGH)
  sleep(delay)
  GPIO.output(STEP, GPIO.LOW)
  sleep(delay)

#PROGRAM DOES ONE CW AND ONE CCW CYCLE
GPIO.cleanup()
