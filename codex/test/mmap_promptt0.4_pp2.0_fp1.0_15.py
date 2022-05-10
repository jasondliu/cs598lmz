import mmap
# Test mmap.mmap()
#
# This is a test for the mmap.mmap() function.
#
# This test does the following:
#     1. Create a file of a specified size.
#     2. Create a memory map of the file.
#     3. Write a byte to the file.
#     4. Read the byte from the memory map.
#     5. If the byte read from the memory map is the same as the byte
#        written to the file, the test passes.
#
# Usage:
#     python mmap_mmap.py <size>
#
# Where <size> is the size of the file to create.
#
# Author: Vasudev Ram
# Copyright 2016 Vasudev Ram
# Web site: https://vasudevram.github.io
# Blog: http://jugad2.blogspot.com
# Product store: https://gumroad.com/vasudevram

import sys
import mmap

def main():
    if len(sys.argv) != 2:
        print("Usage: python mmap_mmap.py <size>")
