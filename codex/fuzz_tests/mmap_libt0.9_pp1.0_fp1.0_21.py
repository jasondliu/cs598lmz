import mmap
import os
import time
import zipfile

# Test
if __name__ == '__main__':
    fd = open("/proc/cpuinfo", "rb")
    map = mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ)
    fd.close()
    map.readline()  # skip the first line
    flag = False
    while True:
        line = map.readline()
        print(line)
        if not line:
            break
        if line.startswith("processor") and flag:
            break
        if line.startswith("processor"):
            flag = True
