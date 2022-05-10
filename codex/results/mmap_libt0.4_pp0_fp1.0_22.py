import mmap
import sys
import os
import re
import subprocess

# if len(sys.argv) != 2:
#     print("Usage: %s <filename>" % sys.argv[0])
#     sys.exit(1)

# filename = sys.argv[1]
# f = open(filename, "r+")
# s = mmap.mmap(f.fileno(), 0)
# print("%d bytes before modification" % s.size())
#
# # memory-map the file, size 0 means whole file
# s.seek(0)  # rewind
# s.write(b"Hello Python!\n")  # modify the file
# print("%d bytes after modification" % s.size())

# s.close()
# f.close()

# f = open(filename, "r+")
# s = mmap.mmap(f.fileno(), 0)
#
# # memory-map the file, size 0 means whole file
# s.seek(0)  # rewind
# print(s.readline()) 
