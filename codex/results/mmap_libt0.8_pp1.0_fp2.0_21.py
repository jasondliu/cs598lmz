import mmap
import ctypes
import csv
import xlwt as xlwt
from serial import *
import binascii

##GLOBAL VARIABLES
row_index = 0
col_index = 0
row_index2 = 0
col_index2 = 0


class SharedMemory(object):
    def __init__(self):
        self.__shm = mmap.mmap(-1, 4096, tagname=u'Local\\MySharedMemory')
        self.__shm.seek(0)
        self.__lock = Lock()

    def Write(self, message):
        self.__lock.acquire()
        try:
            self.__shm.seek(0)
            self.__shm.write(message)
        finally:
            self.__lock.release()

    def Read(self):
        self.__lock.acquire()
        try:
            self.__shm.seek(0)
            return self.__shm.read()
        finally:
            self.__lock.release()

def Serial_
