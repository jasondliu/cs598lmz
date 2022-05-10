import ctypes
import ctypes.util
import threading
import sqlite3 as lite

def getName():
	productnames = []
	filename=[] 
	
	libc = ctypes.CDLL(ctypes.util.find_library('c'))
	libutil = ctypes.CDLL(ctypes.util.find_library('util'))

	disknames = []
	bs_indices = []
	bs_count = 3 
	off_t_real_t = libc.getpagesize()
	bs_count = 3 
	buff = ctypes.c_buffer(bs_count*off_t_real_t)

	indices = ctypes.c_int()
	indices_copy = ctypes.c_int()
	indices = 3
	
	new_disk_name = libc.malloc(1024)
	p_disknames = ctypes.c_int()
	p_bs_indices = ctypes.c_int()
	bs_count = 3 

