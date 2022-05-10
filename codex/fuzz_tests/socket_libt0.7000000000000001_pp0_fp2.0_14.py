import socket
import time
from test import ARDUINO_PORT, ARDUINO_BAUD

from serial import Serial
import serial
from time import sleep
from test import serial_ports

class Arduino:
    def __init__(self, port=ARDUINO_PORT, baud=ARDUINO_BAUD, timeout=1):
        self.serial = Serial(port, baud, timeout=timeout)
        self.timeout = timeout
        self.port = port
        self.baud = baud

    def send(self, msg):
        self.serial.write(msg)

    def receive(self, n=1):
        return self.serial.read(n)

    def close(self):
        self.serial.close()
        del self

    def open(self):
        self.serial = Serial(self.port, self.baud, timeout=self.timeout)

    @property
    def connected(self):
        return self.serial.isOpen()

class ArduinoRemote:
    def __init__(self, host, port=8989):
        self.
