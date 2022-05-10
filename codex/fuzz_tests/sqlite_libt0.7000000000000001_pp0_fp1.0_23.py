import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import inspect
import logging

# import the perl module
perl = ctypes.CDLL(ctypes.util.find_library('perl'))

# define the Perl types
pTHX = ctypes.c_void_p
pTHX_ = ctypes.POINTER(pTHX)
I32 = ctypes.c_int32
pI32 = ctypes.POINTER(I32)
SV = ctypes.c_void_p
pSV = ctypes.POINTER(SV)
AV = ctypes.c_void_p
pAV = ctypes.POINTER(AV)
PV = ctypes.c_char_p
pPV = ctypes.POINTER(PV)
HV = ctypes.c_void_p
pHV = ctypes.POINTER(HV)
CV = ctypes.c_void_p
pCV = ctypes.POINTER(CV)
MAGIC = ctypes.c_void_p
pMAGIC = ctypes.POINTER(MAGIC
