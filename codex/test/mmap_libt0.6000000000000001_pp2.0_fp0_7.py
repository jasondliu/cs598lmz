import mmap
import threading
import time
import numpy as np
import matplotlib.pyplot as plt
import csv

#shared memory
#https://stackoverflow.com/questions/48532523/using-python-shared-memory-for-inter-process-communication

#open shared memory
shm = mmap.mmap(-1, 32, tagname="shared_memory")

#lock the shared memory
lock = threading.Lock()

#set the shared memory to 0
shm.write(b'\x00' * 32)

#close shared memory
shm.close()

#open shared memory
shm = mmap.mmap(-1, 32, tagname="shared_memory")

#lock the shared memory
lock = threading.Lock()

#set the shared memory to 0
shm.write(b'\x00' * 32)

#close shared memory
shm.close()

#open shared memory
shm = mmap.mmap(-1, 32, tagname="shared_memory")

#lock the shared
