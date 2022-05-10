import mmap
from ctypes import *
import time
from tkinter import *

#defining the memory mapped file area
SHM_NAME = "/shm_name"
SHM_SIZE = 1024

class mem_map:
    def __init__(self):
        #setting up the shared memory
        self.shm = mmap.mmap(-1, SHM_SIZE, SHM_NAME, access=mmap.ACCESS_WRITE)

        #setting up the shared memory area to read motors
        self.motors = (c_int16 * 1024).from_buffer(self.shm)
        self.read_motor = 0

        #setting up the shared memory area to write to
        self.write_pointer = (c_int16 * 1024).from_buffer(self.shm)
        self.write_pointer[0] = 0

    def set_motor(self, value):
        #value is from -100 to 100
        #writing to the motor shared memory
        self.motors[1 + self.read_motor] = value
        self.read_
