import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

leds = [24, 25, 8, 7, 12, 16, 20, 21]
aux = [2, 3, 14, 15, 18, 27, 23, 22]

GPIO.setup (leds, GPIO.OUT)
GPIO.setup (aux, GPIO.IN)

try:
    while True:
        for i in range (8):
            GPIO.output (leds[i], GPIO.input (aux[i]))

finally:
    GPIO.output (leds, 0)
