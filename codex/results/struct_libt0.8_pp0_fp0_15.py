import _struct
import socket
import struct
import binascii
import sys
import serial
import time
import datetime
import select
import xbee
import re


# Constants
# Define the ports for xbeeconnect, GPMS and PC
xbeePort = '/dev/ttyUSB0'
GPMSport = '/dev/rfcomm0'
PCport = '/dev/ttyUSB2'

# Define the baud rate for Bluetooth, xbee and PC
baudRate = 9600
xbeeBaud = 9600
PCbaud = 115200

# Define the node addresses for the xbee
gatewayNode = '\x00\x00\x00\x00\x00\x00\xFF\xFF'
MeshNode = '\x00\x13\xA2\x00\x41\x69\x43\xE0'

# Set up the communications with the sensor board
GPMSdev = serial.Serial(port = GPMSport, baudrate = baudRate,
                        bytesize = serial.EIGHTBITS, parity = serial.
