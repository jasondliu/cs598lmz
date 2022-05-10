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

