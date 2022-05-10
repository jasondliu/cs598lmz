import mmap
import sys
import select
import subprocess
import re
import fcntl

def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is

def read_value(file):
    """ read the value of the given file """
    with open(file, "r") as fh:
        return fh.readline()

# make non-blocking so we can time-out on read
def read_with_timeout(file, timeout=0.1):
    """ read the value of the given file with timeout """
    old = fcntl.fcntl(file.fileno(), fcntl.F_GETFL)
    fcntl.fcntl(file.fileno(), fcntl.F_SETFL, old | os.O_NONBL
