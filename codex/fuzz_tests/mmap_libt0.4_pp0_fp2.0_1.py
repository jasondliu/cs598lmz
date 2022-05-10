import mmap
import os
import re
import sys

#------------------------------------------------------------------------------

def usage():
    print "Usage: %s <file> <regex>" % sys.argv[0]
    sys.exit(1)

#------------------------------------------------------------------------------

def main():
    if len(sys.argv) != 3:
        usage()

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print "File '%s' does not exist" % filename
        sys.exit(1)

    regex = re.compile(sys.argv[2])

    f = open(filename, "r")
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    for match in regex.finditer(m):
        print match.group(0)

    m.close()
    f.close()

#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------
