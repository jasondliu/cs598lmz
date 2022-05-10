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
