import _struct
import os,sys

OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def parse_memmap(memmap):
	memmap_file = open(memmap, "rb") # Open memmap in read-binary mode
	data = memmap_file.read()
	memmap_file.close()
	types = _struct.unpack('<1020L', data[:4080]) # Unpack header
	set_names = data[4096:8192].split('\x00')[:-1] # Read names
	data_sets = [] # Create empty list for data
	for i in xrange(0, 1020):
		offset = 8192 + (types[i]*4) # calculate first offset for data was added in python 2.6
		name = set_names[i] # add data name:
		data_sets.append([name, []]) # add name
