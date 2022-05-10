import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import os
#
# Debugging
#
import pdb
import platform
#
#
#
import multiprocessing

#
#
#
def debug(st):
    if debug:
        print(st)


#
#
#
def stop(st):
    if stop():
        print(st)
        sys.exit(1)


#
#
#
def get_samples_from_file(filename):
    with open(filename, 'r') as fin:
        samples = fin.read().splitlines()
    return samples

#
#
#
def get_samples_from_file_list(file_list):
    samples = []
    for filename in file_list:
        samples.extend(get_samples_from_file(filename))
    return samples

#
#
#
def get_samples_from_list(list_of_samples):
    samples = []
    samples.extend([line.rstrip('\n') for line in list_of_samples])
    return samples


