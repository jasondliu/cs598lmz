import mmap
import hashlib
import os

# This script will take a file and a byte offset, and give you the md5sum of the first chunk

usage = "Usage: %prog [options] -f FILE -o OFFSET"
