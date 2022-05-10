import mmap
# Test mmap.mmap
m = mmap.mmap(0,4096,tagname='tag')
m

import os
m = mmap.mmap(os.getpid(),4096,tagname='tag')
m

m = mmap.mmap(os.getpid(),4096,access=mmap.ACCESS_COPY,tagname='tag')
m

m = mmap.mmap(os.getpid(),4096,access=mmap.ACCESS_READ,tagname='tag')
m

m = mmap.mmap(os.getpid(),4096,access=mmap.ACCESS_WRITE,tagname='tag')
m

m = mmap.mmap(os.getpid(),4096,access=mmap.ACCESS_READ|mmap.ACCESS_WRITE,tagname='tag')
m

m = mmap.mmap(os.getpid(),4096,access=mmap.ACCESS_DEFAULT,tagname='tag')
m
