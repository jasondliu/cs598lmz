import mmap
import struct
import sys
import os

#
# This is a simple python script to read the data from the shared memory buffer
# created by the C++ program.
#
# The C++ program creates a shared memory buffer and writes a series of
# integers to it.  This python script reads the shared memory buffer and
# prints the integers to the screen.
#

#
# This is the name of the shared memory buffer created by the C++ program.
#
SHARED_MEMORY_NAME = "MySharedMemory"

#
# This is the name of the semaphore created by the C++ program.  This
# semaphore is used to coordinate access to the shared memory buffer.
#
SEMAPHORE_NAME = "MySemaphore"

#
# This is the size of the shared memory buffer.
#
BUFFER_SIZE = 4096

#
# This is the number of integers in the shared memory buffer.
#
NUM_INTEGERS = int(BUFFER_SIZE / 4)

#
# This is the number of times to read the shared memory buffer.
