import mmap
import os
import sys

def write_file(file_name, data):
    fd = os.open(file_name, os.O_RDWR | os.O_CREAT)
    os.write(fd, data)
    os.close(fd)

def read_file(file_name):
    fd = os.open(file_name, os.O_RDWR | os.O_CREAT)
    data = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_WRITE)
    os.close(fd)
    return data

