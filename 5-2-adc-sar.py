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
    value = 0
    for i in range (8):
        value = value + 2**(7 - i)
        signal = bin2dac(value)
        time.sleep(0.01)
        compV = GPIO.input(comp)
        if compV == 0:
            value = value - 2**(7 - i)
        
        volt = value / level * mU
        print ("Digital value: {:^3} -> {}, Analog value: {:.2f}".format(value, signal, volt))

    

try:
    while True:
        adc()

finally:
    GPIO.cleanup ()