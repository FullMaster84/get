import RPi.GPIO as GPIO
import time


dac = [26, 19, 13, 6, 5, 11, 9 , 10]
comp = 4
troyka = 17
bits = 8
level = 2**bits
mU = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(bits)]

def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output (dac, signal)
    return signal

def adc():
    for value in range (256):
        signal = bin2dac(value)
        volt = value / level * mU
        time.sleep(0.001)
        compValue = GPIO.input (comp)
        if compValue == 0:
            print ("Digital value: {:^3} -> {}, Analog value: {:.2f}".format(value, signal, volt))
            break

try:
    while True:
        adc()

finally:
    GPIO.cleanup ()
    GPIO.cleanup (dac)



