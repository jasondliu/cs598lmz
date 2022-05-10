import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/pi/Desktop/test.db')

# Initialize the library to use the local gpio pins on the Pi
# lib = ctypes.CDLL(ctypes.util.find_library('wiringPi'))
# lib.wiringPiSetup()

# Initialize the library to use the local gpio pins on the Pi
# lib = ctypes.CDLL(ctypes.util.find_library('wiringPi'))
# lib.wiringPiSetup()

# Create a lock to prevent multiple threads from accessing the same GPIO pins at once
lock = threading.Lock()

# This class handles the communication with the GPIO pins
class I2C:
    # Initialize the class.
    # The "address" parameter is the I2C address of the device.
    # The "bus" parameter is the I2C bus to use.
    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)

    # Write a single command
