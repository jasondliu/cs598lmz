import mmap
import struct
from datetime import datetime
import math
import sys

if len(sys.argv) < 2:
    print "Usage: " + sys.argv[0] + " <file>"
    sys.exit(1)

lines = []

f = open(sys.argv[1], "rb")
map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

while True:
    line = map.read(136)
    if len(line) != 136:
        break
    lines.append(line)

map.close()
f.close()

lines.sort(key=lambda x: struct.unpack("<I", x[:4])[0])

min_t = struct.unpack("<I", lines[0][:4])[0]
max_t = struct.unpack("<I", lines[-1][:4])[0]

print "Minimum time: " + datetime.fromtimestamp(min_t).strftime("%Y-%m-
