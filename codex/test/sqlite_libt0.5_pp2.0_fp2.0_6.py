import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import subprocess

# Loading the C library

libc = ctypes.CDLL(ctypes.util.find_library("c"))

# Defining the functions in the C library

libc.getpid.restype = ctypes.c_uint
libc.getpid.argtypes = ()

libc.getppid.restype = ctypes.c_uint
libc.getppid.argtypes = ()

libc.getuid.restype = ctypes.c_uint
libc.getuid.argtypes = ()

libc.geteuid.restype = ctypes.c_uint
libc.geteuid.argtypes = ()

libc.getgid.restype = ctypes.c_uint
libc.getgid.argtypes = ()

libc.getegid.restype = ctypes.c_uint
libc.getegid.argtypes = ()

# Creating the database

conn = sqlite3.connect("/var/tmp/monitor.db")
cursor = conn.c
