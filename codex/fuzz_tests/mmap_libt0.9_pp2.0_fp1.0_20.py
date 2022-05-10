import mmap
import os
import sys
import time

def scan_uselist(dir):
	global page_size
	global page_offset
	global page_hashsize
	start = time.time()

	hashsize = {}
	offset = {}
	size = {}
	
	# scan files in dir
	for file in os.listdir(dir):
		if not file.endswith('.uselist'):
			continue

		# save file descripter
		fd = open(dir+'/'+file, 'rb')

		# get file size
		fd.seek(0,2)
		file_size = fd.tell()
		fd.seek(0)
	
		# mmap file
		mm = mmap.mmap(fd.fileno(), file_size, access=mmap.ACCESS_READ)

		# print file name
		print '%s: ' % file

		# count page
		count = file_size / page_size

		# get hashsize
	
