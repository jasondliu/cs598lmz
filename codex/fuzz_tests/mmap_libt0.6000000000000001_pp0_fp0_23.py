import mmap
import ctypes
import numpy
import time
import math

#This is the name of the shared memory block that the simulator uses to communicate with the python script
#You must change this to match your python script in the simulator
#This has to be changed in both the Python script and the Simulator
name = "sharedMemory"

#This is the name of the semaphore used to coordinate access to shared memory
semName = "sharedMemorySem"

#This is the memory size of the shared memory
memSize = 65536

#This is the number of floating point values that the shared memory contains
floatCount = 2048

#This is the number of integer values that the shared memory contains
intCount = 2048

#This is the number of boolean values that the shared memory contains
boolCount = 2048

#This is the number of string values that the shared memory contains
stringCount = 2048

#This is the size of the string values in bytes
stringSize = 256

#This is the size of the shared memory in bytes
memSizeInBytes = memSize

#This is the semaphore used to coordinate access to shared memory

