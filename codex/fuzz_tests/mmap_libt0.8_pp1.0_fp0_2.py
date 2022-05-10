import mmap
import subprocess
import sys

# The main driver
def main():
	# Read the command line arguments
	if len(sys.argv) < 3:
		print 'Usage: python gzipsort.py file.gz memory_size(MB)'
		return
	# Open the gzipped file
	with gzip.open(sys.argv[1]) as gz_file:
		# Run gzipsort
		gzipsort(gz_file, int(sys.argv[2]))

# Sort a gzipped file in-place
def gzipsort(gz_file, memory_size=64):
	# The size of the file in bytes
	# Use memory-mapped files
	# Map the file as if it were not gzipped
	mm_file = mmap.mmap(gz_file.fileno(), 0, access=mmap.ACCESS_READ)
	# Get the number of lines in the file
	# This is used to know how large each block should be
	num_lines = mm_file.size(
