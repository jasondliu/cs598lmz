import bz2
bz2.decompress(compressed)

class Recurse(object):
    def __del__(self):
        print 'Recurse.__del__'
        del self.self

Recurse().self = Recurse()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.output(12,False)
GPIO.output(13,False)
GPIO.output(18,False)
GPIO.output(19,False)
time.sleep(1)
GPIO.output(12,True)
GPIO.output(13,True)
GPIO.output(18,True)
GPIO.output(19,True)
