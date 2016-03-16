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

GPIO.setup(13, GPIO.OUT)  # Set pin mode as output
GPIO.output(13, GPIO.HIGH)

try:
    print "hej"
    while True:
        d = checkdist()
        print d
        if d < 0.6:
            print 'Distance: %0.2f m' % d
            GPIO.output(13, GPIO.LOW)
            print "led on"
            time.sleep((d / 0.6) * 2)
            GPIO.output(13, GPIO.HIGH)
            print "led off"
        else:
            GPIO.output(13,GPIO.LOW)



except KeyboardInterrupt:
    GPIO.cleanup()
