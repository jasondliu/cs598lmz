import mmap
import math
import sys
import multiprocessing
import concurrent.futures

def worker_f(block, pattern_fn, comp_tool, i ):
	if not os.path.exists(block):
		print "ERROR: file " + block + " not found"
		sys.exit(0)

	file1_name = block
	file2_name = pattern_fn

	if comp_tool == "bz2":
		bz_command1 = "bunzip2 -c " + file1_name + " | "
		bz_command2 = "bunzip2 -c " + file2_name + " | "
		file1_name = "/proc/self/fd/0"
		file2_name = "/proc/self/fd/0"
	elif comp_tool == "LZW":
		bz_command1 = "lzwcat "  + file1_name + " | "
		bz_command2 = "lzwcat "  + file2_name + " | "
