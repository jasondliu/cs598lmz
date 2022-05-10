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

def main():
    if len(sys.argv) < 2:
        print "Usage: %s file_name" % sys.argv[0]
        sys.exit(1)

    file_name = sys.argv[1]
    write_file(file_name, "hello world")
    data = read_file(file_name)
    print "Before:", data
    data[0:5] = "HELLO"
   
