import select
import sys
import time

import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff = 0
ser.rtscts = 0
ser.timeout = 20
ser.port = "/dev/ttyUSB0"

try:
    ser.open()
except Exception, e:
    print "error open serial port: " + str(e)
    exit()

if ser.isOpen():
    try:
        ser.flushInput()
        ser.flushOutput()
        time.sleep(0.5)
        response = ser.readlines()
        #print response
    except Exception, e1:
        print "error communicating...: " + str(e1)
else:
    print "cannot open serial port "

print ser.isOpen()

while True:
    try:
        in_command = raw_input("Enter command or 'exit':
