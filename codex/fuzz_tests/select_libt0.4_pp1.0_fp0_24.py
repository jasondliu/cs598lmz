import select
import sys
import time
import pdb
import os
import signal
import subprocess
import re
import json

import serial
import serial.tools.list_ports

import logging

#logging.basicConfig(level=logging.DEBUG)

from threading import Thread
from queue import Queue

class SerialPort:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.serial = serial.Serial(port, baudrate)

    def read(self, size=1):
        return self.serial.read(size)

    def write(self, data):
        return self.serial.write(data)

    def inWaiting(self):
        return self.serial.inWaiting()

    def flush(self):
        return self.serial.flush()

    def flushInput(self):
        return self.serial.flushInput()

    def flushOutput(self):
        return self.serial.flushOutput()

    def close(self):
        self.serial.close
