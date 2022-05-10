import select
import serial
import sys
import os

ser = serial.Serial('/dev/ttyACM0',9600)
ser.flush()

path=sys.argv[1]

def readFromArduino():
    while True:
        try:
            l = ser.readline().strip()
            print l
        except:
            print "Did not work"
            time.sleep(1)

def writeToArduino():
    while True:
        try:
            line = raw_input()
            ser.write(line)
            print "yay sent"
        except:
            print "Did not work"
            time.sleep(1)

if __name__ == '__main__':
    readFromArduino()
    #writeToArduino()
