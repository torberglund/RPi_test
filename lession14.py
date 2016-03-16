#! /usr/bin/python
import RPi.GPIO as GPIO
import time


def checkdist():
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(16, GPIO.LOW)
    while not GPIO.input(18):
        pass
    t1 = time.time()
    while GPIO.input(18):
        pass
    t2 = time.time()
    return (t2 - t1) * 340 / 2


GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.IN)
time.sleep(2)

GPIO.setup(11, GPIO.OUT)   # Set pin mode as output
GPIO.output(11, GPIO.HIGH)


try:
    while True:
        d= checkdist()
        if d<0.30 :
            print 'Distance: %0.2f m' % d
            GPIO.output(13, GPIO.LOW)
            time.sleep((d/0.30)*1)
            GPIO.output(13, GPIO.HIGH)


except KeyboardInterrupt:
    GPIO.cleanup()
