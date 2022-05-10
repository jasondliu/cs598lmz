import select
import serial
import sys
import os

ser = serial.Serial('/dev/ttyACM0',9600)
ser.flush()

path=sys.argv[1]

