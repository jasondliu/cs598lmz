import mmap
# Test mmap.mmap.find_pattern and mmap.mmap.find_bytes.
# Print the memory address of the first and last occurence of the pattern.
# If it does not occur, print the first and last address which can be matched
#   in the mmap'ed memory.
# Added robustness in tests by mmapping a RAM file instead of the path.
#############################################
import os
import platform
import subprocess
import mmap
import io
from ELF import *

def main():
    ifile = sys.argv[1]
    pattern = sys.argv[2]
    elf = ELF(ifile)
    mm = elf.mmap_file()
    ptr_mmap = mm.find_pattern(pattern)
    print("Found pattern at:", ptr_mmap)
    utils.p("Finding bytes in memory.....")
    ptr_bytes = mm.find_bytes(pattern.encode() )
    print("Found bytes at:", ptr_bytes)
    mm.close()
    return

if __name__ == "__main__":
    main()
