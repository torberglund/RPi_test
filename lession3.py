#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BZRPin = 11


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers pins by physical location
    GPIO.setup(BZRPin, GPIO.OUT)  # Set pin mode as output
    GPIO.output(BZRPin, GPIO.LOW)


    p = GPIO.PWM(BZRPin, 50)  # init frequency: 50HZ
    p.start(50)  # Duty cycle: 50%


def loop():
    f=100
    while True:
        tx = input()
        if tx <=20 and tx >=1:
            p.ChangeFrequency(f*tx)
        if tx==0:
            destroy()


def destroy():
    p.stop()
    GPIO.cleanup()


if __name__ == '__main__':  # Program start from here
    print 'Press Ctrl+C to end the program...'
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
