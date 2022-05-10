import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# import sys
# sys.path.append("/home/pi/Desktop/python/python-xbee-api-master")
# from xbee import ZigBee

# import serial
# ser = serial.Serial('/dev/ttyUSB0', 9600)

# XBee setting
# PORT = '/dev/ttyUSB0'
# BAUD_RATE = 9600

# Open serial port
# ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
# xbee = ZigBee(ser, escaped=True)

# Define callback function
# def message_received(data):
#     print(data)

# Set callback function
# xbee.on_data_received = message_received

# Do other stuff in the main thread
# while True:
#     try:
#         time.sleep(0.1)
#     except KeyboardInterrupt:
#         break

# Halt() must be called before closing the serial
# port in order to ensure proper thread shutdown
# xbee.halt()

