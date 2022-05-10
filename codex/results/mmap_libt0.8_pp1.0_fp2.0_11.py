import mmap
import sys

if len(sys.argv) < 2:
    print("usage: python3 mygrep.py [file] [string]")
    sys.exit()

try:
    f = open(sys.argv[1], "r+")
except IOError as e:
    print("no such file")
    sys.exit()

s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if s.find(sys.argv[2].encode()) != -1:
    print("true")
else:
    print("false")
s.close()
f.close()
