import RPi.GPIO as GPIO

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
    while True:
        inpStro = input ("Ввод числа от 0 до 255\n Если вы дед инсайд нажмите 'q' \n")

        if inpStro.isdigit():
            value = int(inpStro)
            if value >= lev:
                print ("Err")
                continue
            signOUT(value)
            Udac = maxU / 256 * int(inpStro)
            print (str(Udac) + 'v')
        
        elif inpStro == 'q':
            break
        
        else:
            print ("Err")


finally:
    GPIO.output(dac, 0)
