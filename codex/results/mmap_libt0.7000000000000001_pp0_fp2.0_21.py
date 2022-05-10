import mmap
import sys

if len(sys.argv) < 2:
    print >> sys.stderr, "Usage:", sys.argv[0], "<file>"
    sys.exit(1)

f = open(sys.argv[1])
try:
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    while True:
        line = s.readline()
        if not line:
            break
        print line,
finally:
    f.close()
