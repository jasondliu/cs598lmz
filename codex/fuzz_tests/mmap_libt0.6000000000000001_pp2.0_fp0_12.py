import mmap
import array
import os
import time
import math
import sys

#config

#block size in bytes, must be a multiple of the page size
block_size = 4096*128

#file size in bytes
file_size = 4096*1024*1024*100

#number of read/write operations
read_write_ops = 10000

#end config

#check if the files are already there
if os.path.exists("test_mmap.bin"):
    print "test_mmap.bin already exists, please remove it first!"
    exit()

if os.path.exists("test_seq.bin"):
    print "test_seq.bin already exists, please remove it first!"
    exit()

if os.path.exists("test_rand.bin"):
    print "test_rand.bin already exists, please remove it first!"
    exit()

#determine the page size
page_size = os.sysconf("SC_PAGE_SIZE")

if block_size % page_size != 0:
    print "block size not
