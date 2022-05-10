import mmap
from datetime import datetime
import time
from subprocess import Popen, PIPE
from os import listdir
from os.path import isfile, join
import sys
import subprocess
from collections import OrderedDict

# Global variables

# Global variables

# The size of the shared memory block
# This must be the same as the size that the server uses
shmSize = 1024

# The name of the shared memory block
# This must be the same as the name that the server uses
shmName = "OSLab4SharedMemory"

# The data file containing the account information
dataFileName = "accounts.txt"

accounts = {}

# This is the key for the semaphore used to control access to the shared memory
semKey = 5678

# This is the key for the semaphore used to control access to the shared memory
shmKey = 1234

# This is the semaphore used to control access to the shared memory
sem = None

# This is the shared memory block
shm = None


def main():
    global sem
   
