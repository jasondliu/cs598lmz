import mmap
import sys
import os

mem = mmap.mmap(-1, 100000, "MySharedMemory", mmap.ACCESS_WRITE)
try:
    print mem.readline()
    print mem.readline()
finally:
    mem.close()
'''

import mmap
import sys
import os

mem = mmap.mmap(-1, 1000, "MySharedMemory")

try:
    mem.write('hello')
except:
    print 'unable to write'
    pass
else:
    print 'written'

try:
    print mem.read(5)
except:
    print 'unable to read'
    pass
else:
    print 'read'
finally:
    mem.close()
