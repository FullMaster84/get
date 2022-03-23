import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)


dac = [26, 19, 13, 6, 5, 11, 9, 10]
bit = len(dac)
lev = 2**bit
maxU = 3.3

GPIO.setup (dac, GPIO.OUT, initial = GPIO.LOW)

def dec2bin (value):
    return [int(bin) for bin in bin(value)[2:].zfill(bit)]

def signOUT(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)

try:
    Peroid = input ("Ввод периода\n")
    t = int(Peroid) / (2*255)  

    for i in range (255):
        signOUT(i)
        time.sleep(t)
    i = 255
    while i >= 0:
        signOUT(i)
        time.sleep (t)
        i = i - 1

finally:
    GPIO.output (dac, 0) 