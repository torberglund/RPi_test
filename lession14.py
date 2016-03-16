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

GPIO.setup(7, GPIO.OUT)   # Set pin mode as output
GPIO.output(7, GPIO.LOW)

p = GPIO.PWM(7, 50) # init frequency: 50HZ
p.start(50)  # Duty cycle: 50%
try:
    while True:
        d= checkdist()
        print d
        if d<0.25 :
            print 'Distance: %0.2f m' % checkdist()
            p.ChangeFrequency((1-(d/0.30))*400)

except KeyboardInterrupt:
    GPIO.cleanup()
