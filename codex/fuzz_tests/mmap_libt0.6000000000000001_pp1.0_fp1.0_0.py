import mmap
import os
from struct import *
import sys
import time

# ------------------------------------------------------------------------------
# Read a single byte from the I2C device
# ------------------------------------------------------------------------------
def read_byte(address):
    return bus.read_byte_data(address, 0)

# ------------------------------------------------------------------------------
# Read a single word from the I2C device
# ------------------------------------------------------------------------------
def read_word(address):
    high = bus.read_byte_data(address, 0)
    low = bus.read_byte_data(address, 1)
    val = (high << 8) + low
    return val

# ------------------------------------------------------------------------------
# Read a single word from the I2C device
# ------------------------------------------------------------------------------
def read_word_2c(address):
    val = read_word(address)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

# ------------------------------------------------------------------------------
# Read a block of data from the I2C device
# ------------------------------------------------------------------------------
def read_block(address, num):
    # Read a block of data
    data = bus.read_
