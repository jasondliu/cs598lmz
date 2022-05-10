import mmap
# Test mmap.mmap()
#
# http://docs.python.org/library/mmap.html
# http://stackoverflow.com/questions/21334739/how-to-use-the-python-mmap-module
#
#
import sys
from os import strerror
from mmap import mmap,ACCESS_READ

print("\n===== Test mmap.mmap() =====")

def mmap_test(filename):
    try:
        fd = open(filename,"r+b")
    except IOError as e:
        print("Unable to open the file:", strerror(e.errno))
        return
    try:
        m = mmap(fd.fileno(), 0, access=ACCESS_READ)
    except ValueError as e:
        print("mmap", strerror(e.errno))
        return
    print("mmap:", m[:20], "...", m[-20:])
    print("filename:", filename)
    fd.close()
    m.close()

