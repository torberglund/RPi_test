#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


BeepPin = 11  # pin11


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers pins by physical location
    GPIO.setup(BeepPin, GPIO.OUT)  # Set pin mode as output
    GPIO.output(BeepPin, GPIO.HIGH)  # Set pin to high(+3.3V) to off the beep



def loop():
    while True:
        tx = raw_input()
        if tx=="1":
            GPIO.output(BeepPin, GPIO.LOW)
        else:
            GPIO.output(BeepPin, GPIO.HIGH)

def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)  # beep off
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    print 'Press Ctrl+C to end the program...'
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
