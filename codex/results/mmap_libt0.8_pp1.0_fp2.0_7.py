import mmap
import struct
import os
import sys

if len(sys.argv) != 2:
    print "Usage:",sys.argv[0],"<file>"
    quit()

file=sys.argv[1]

if not os.path.isfile(file):
    print "Error: must specify a file"
    quit()

with open(file, "rb") as f:
    # open file and mmap it
    mm = mmap.mmap(f.fileno(), 0)
    # seek to 0x300
    mm.seek(0x300)
    # read size of main table
    main_table_size=struct.unpack("<I", mm.read(4))[0]
    # seek to 0x400
    mm.seek(0x400)
    # read size of second table
    second_table_size=struct.unpack("<I", mm.read(4))[0]
    # seek to 0x600
    mm.seek(0x600)
    # read size of third table
    third_table_
