#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


class keypad():
    # CONSTANTS
    KEYPAD = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]

    ]
    BZRPin = 7
    RedPin=7
    GreenPin=15
    ROW = [11, 12, 13]
    COLUMN = [16, 18, 22]

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

    def getKey(self):

        # Set all columns as output low
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)


        # Set all rows as input
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i

        # if rowVal is not 0 thru 3 then no button was pressed and we can exit
        if rowVal < 0 or rowVal > 3:
            self.exit()
            return -1

        # Convert columns to input
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Switch the i-th row found from scan to output
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)

        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 2.
        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal = j

        # if colVal is not 0 thru 2 then no button was pressed and we can exit
        if colVal < 0 or colVal > 2:
            self.exit()
            return -1

        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[rowVal][colVal]

    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def setupPins(self):
        GPIO.setmode(GPIO.BOARD)  # Numbers pins by physical location
        GPIO.setup(self.RedPin, GPIO.OUT)  # Set pin mode as output
        GPIO.output(self.RedPin, GPIO.HIGH)
        GPIO.setup(self.GreenPin, GPIO.OUT)  # Set pin mode as output
        GPIO.output(self.GreenPin, GPIO.HIGH)

    def checkpass(self):
        pressed=[0,0,0,0]
        passw=[1,2,3,4]
        digit=-1
        for i in range (0,4):
            while digit == -1:
                digit=self.getKey()

            print "you pressed" +str(digit)
            print "assigning "+str(digit)+" at position "+str(i)
            pressed[i]=digit
            while digit != -1:
                digit = self.getKey()


        # Print the result
        if pressed !=passw:
            print str(pressed)+" does not match password"
            return False
        else:
            print "matches password"
            return True

    def destroy(self):
        GPIO.output(self.GreenPin, GPIO.HIGH)
        GPIO.output(self.RedPin, GPIO.HIGH)# beep off
        GPIO.cleanup()  # Release resource







if __name__ == '__main__':

    # Initialize the keypad class
    kp = keypad()
    kp.setupPins()
    # Loop while waiting for a keypress
    try:
        while True:

            if kp.checkpass()==False:
                print "playing error sound"
                GPIO.output(kp.RedPin, GPIO.LOW)
                time.sleep(1)
                GPIO.output(kp.RedPin, GPIO.HIGH)
            else:
                print "playing success sound"
                GPIO.output(kp.GreenPin, GPIO.LOW)
                time.sleep(1)
                GPIO.output(kp.GreenPin, GPIO.HIGH)
    except KeyboardInterrupt:
        kp.destroy()

