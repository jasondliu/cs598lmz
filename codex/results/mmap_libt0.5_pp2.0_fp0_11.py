import mmap
import sys
import time
import os
import struct
import math

class Barometer:
    def __init__(self, bus, addr=0x60, calibration_file="/root/barometer_calibration.txt"):
        self.bus = bus
        self.addr = addr
        self.calibration_file = calibration_file
        self.load_calibration()

    def load_calibration(self):
        try:
            with open(self.calibration_file, "r") as f:
                self.calibration = [float(x) for x in f.readline().split(",")]
        except IOError:
            self.calibration = None

    def write_calibration(self):
        if self.calibration is None:
            return
        try:
            with open(self.calibration_file, "w") as f:
                f.write(",".join(str(x) for x in self.calibration))
        except IOError:
            pass

    def get_calibration(self
