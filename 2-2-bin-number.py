import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

dac = [10, 9, 11, 5, 6, 13, 19, 26]
number = [0, 0, 0, 0, 0, 0, 1, 0]

GPIO.setup (dac, GPIO.OUT)
GPIO.output (dac, number)
time.sleep (15)
GPIO.output (dac, 0)

GPIO.cleanup ()
