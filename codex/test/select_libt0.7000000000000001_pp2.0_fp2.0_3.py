import select
import serial
import time

class Arduino:
    def __init__(self, port, baud=115200, timeout=2, read_bytes=1):

        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.read_bytes = read_bytes
        self.ser = None

    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baud, timeout=self.timeout)
            print("Arduino connected.")
        except:
            print("Unable to connect to Arduino.")
            pass

    def is_connected(self):
        if self.ser is not None:
            return True
        else:
            return False
