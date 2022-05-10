import mmap
# Test mmap.mmap.readline()
#
# This script uses the mmap module to read a file line by line.
# It is a good example of the use of mmap.mmap.readline().
#
# This script was originally written by Andrew Dalke and is
# re-released here under the same license as mmap.py.
#
# - Gordon McMillan, 22 Aug 2002

import mmap, sys, string

def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print "Usage: read_mmap.py filename"
        sys.exit(2)

    f = open(filename, 'r+')
    # memory-map the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0)
    while True:
        line = m.readline()
        if not line: break
        print repr(line)
    m.close()
    f.close()

if __name__ == '__main__':
    main()
