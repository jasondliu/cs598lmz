import mmap
import os
import time
from collections import deque

# Get temperature from channel 0 in degrees C
def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(device_file):
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(device_file)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = c_to_f(temp_c)
        #return temp_c, temp_f
        return temp_f

def read
