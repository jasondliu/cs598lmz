import mmap
import sys
import time
import os

#
# This is a simple example of how to use the mmap module.
#
# See the test/test_mmap.py file for a more complete set of tests.
#

def main():
    # Open file
    fd = os.open("/tmp/mmaptest", os.O_RDWR | os.O_CREAT)

    # Zero out the file to insure it's the right size
    assert os.write(fd, b"\x00" * mmap.ALLOCATIONGRANULARITY) == mmap.ALLOCATIONGRANULARITY

    # Create the mmap instace with the following params:
    # fd: File descriptor which supports mmap() method
    # length: Must be a multiple of ALLOCATIONGRANULARITY (see Python's mmap
    #     documentation for ALLOCATIONGRANULARITY)
    # flags: MAP_SHARED means other processes can share this mmap
    # prot: PROT_WRITE means this process can write to this mmap
    size = mmap.ALLOC
