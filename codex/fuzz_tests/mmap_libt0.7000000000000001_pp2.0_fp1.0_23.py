import mmap
import os
import sys
import time
import win32con
import win32file
import winerror
import winioctlcon

class win32_file:
	def __init__(self, path):
		self.path = path
		self.handle = None
		self.file_size = None
		self.is_write = None
		self.is_read = None

	# Open file
	def open(self, write=False, read=False):
		self.is_write = write
		self.is_read = read
		if self.is_write and self.is_read:
			self.handle = win32file.CreateFile(self.path, win32con.GENERIC_READ | win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ, None, win32con.OPEN_ALWAYS, 0, None)
		elif self.is_write:
			self.handle = win32file.CreateFile(self.path, win32con.GENERIC_WR
