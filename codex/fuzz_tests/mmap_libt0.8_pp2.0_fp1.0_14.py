import mmap
import time
import sys

if len(sys.argv) != 2:
	print("You must enter a filename")
	sys.exit(0)

filename = sys.argv[1]

with open(filename, 'r') as f:
	print("Opening " + filename)
	mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
	while True:
		line = mm.readline()
		print(line)
		time.sleep(1)
