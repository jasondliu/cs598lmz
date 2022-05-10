import mmap
# Test mmap.mmap(0, 0)

import mmap
import struct

def display(m):
  print 'mmap length        :', len(m)
  print 'mmap size          :', m.size()
  print 'mmap fileno        :', m.fileno()
  print 'mmap offset        :', m.offset()
  print 'mmap itemsize      :', m.itemsize
  print 'mmap readable      :', m.readable()
  print 'mmap writable      :', m.writable()
  print 'mmap seekable      :', m.seekable()

# Test map of all 0s
m = mmap.mmap(0, 0)
print 'mmap of 0s'
print '----------'
display(m)

# Test map of all 1s
m = mmap.mmap(0, 0, 1)
print 'mmap of 1s'
print '----------'
display(m)

# Test map of all 0xffs
m = mmap.mmap(0, 0, 255)
print 'mmap of 0
