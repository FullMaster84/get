import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

comp = 4
troyka = 17
maxvolt = 3.3

GPIO.setmode(GPIO.BCM)


dac  = [26, 19, 13, 6, 5, 11, 9, 10]
null = [ 0,  0,  0, 0, 0,  0, 0,  0]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
data = [0]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)


def dec2bin (val):
    return bin(val)[2:].zfill(8)

def bin2gpio (val):
    bin = [int (elem) for elem in dec2bin(val)]
    GPIO.output(dac, bin)
    return bin

def bin2leds (val):
    bits = 0
    null = [0, 0, 0, 0, 0, 0, 0, 0]
    bits = int (8 * val / 256)
    for i in range (bits):
        null[i] = 1
    GPIO.output(leds, null)

def adc():
    for value in range(256):
        signal = bin2gpio(value)
        time.sleep(0.001)
        volt = value / 256 * maxvolt
        compval = GPIO.input(comp)
        if compval == 0:
            return value

try:
    time_init = time.time()
    value = adc ()
    print ("Зарядка конденсатора с напряжения: {:.4} V" .format(value / 256 * 3.3))
    while value < 240:
        value = adc ()
        bin2leds(value)
        data.append(value / 256 * 3.3)
        

    GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)

    print ("Разрядка конденсатора с напряжения: {:.4} V" .format(value / 256 * 3.3))
    while value > 5:
        value = adc ()
        bin2leds(value)
        data.append(value / 256 * 3.3)
    print ("НАпряжение в конце: {:.2} V" .format(value / 256 * 3.3))

    time = time.time()
    data_str = [str(item) for item in data]
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(data_str))

    time = time - time_init
    print ("Общее время: {:.3} c" .format(time))
    print ("Период шага: {:.3} c" .format(0.001))
    print ("Частота средняя: {:^3} КГц". format(1))
    print ("Шаг квантования: {:.3} В" .format(3.3 / 256))

    plt.plot(data)
    plt.show()

except KeyboardInterrupt:
    print ('\n INPUT ERROR')
    GPIO.cleanup()

finally:
    GPIO.output(dac, null)
    GPIO.cleanup()
