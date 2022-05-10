import mmap
# Test mmap.mmap (mapping) memory
from sys import argv
from random import random

filename = "data.dat"
n = 100 * 1024 * 1024

def create_and_write_data():
    l = [random() for i in range(n)]
    f = open(filename, "w+b")
    data = array("d", l)
    data.tofile(f)

def view_data(bytes):
    size = 13 * 8
    f = open(filename, "rb")
    buf = mmap.mmap(f.fileno(), size, mmap.MAP_SHARED, mmap.PROT_READ)
    buf[bytes:bytes+8]
    buf.close()

def update_data(bytes):
    size = 13 * 8
    f = open(filename, "r+b")
    buf = mmap.mmap(f.fileno(), size, mmap.MAP_SHARED, mmap.PROT_WRITE)
    buf[bytes:bytes+8] = array("d", [42])
    buf.close()
