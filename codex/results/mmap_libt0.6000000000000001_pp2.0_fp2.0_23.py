import mmap
import sys
import struct
import time

# GLOBALS
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------

def help():
    print("Usage:")
    print("\tpython3 %s <file> <offset> <size> <word>" % sys.argv[0])
    print("\t\t<file>\t\t: file to dump")
    print("\t\t<offset>\t\t: offset to start reading")
    print("\t\t<size>\t\t: number of bytes to read")
    print("\t\t<word>\t\t: 4 bytes word to search")
    print("\t\t<output_file>\t: output file to write the dump")
    exit(1)

# ------------------------------------------------------------------------------

if len(sys.argv) != 6:
    help()

file_name = sys.argv[1]
offset = int(sys.argv[2], 16)
size = int(sys.argv[3], 16)
word = sys.argv[4]
output
