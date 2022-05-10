import mmap
import os
import time
import sys

#
# A simple class that wraps the mmap functionality
#
class mmap_wrapper:
    #
    # Initialize the class.  This is called by __init__
    #
    def init(self, filename, access):
        self.access = access
        self.filename = filename
        self.file_size = os.path.getsize(filename)
        self.fd = os.open(filename, os.O_RDWR)
        self.map = mmap.mmap(self.fd, self.file_size, access=access)
        self.pos = 0

    #
    # Initialize the class.  This is called by __init__
    #
    def __init__(self, filename, access=mmap.ACCESS_COPY):
        self.init(filename, access)

    #
    # Close the class.  This is called by __del__
    #
    def close(self):
        self.map.close()
        os.close(self.fd)

    #
    #
