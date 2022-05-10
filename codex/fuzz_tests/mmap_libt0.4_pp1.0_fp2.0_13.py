import mmap
import os
import sys
import time

def main(argv):
    if len(argv) != 2:
        print("Usage: %s <filename>" % argv[0])
        return 1

    filename = argv[1]

    # Open the file for reading
    fd = os.open(filename, os.O_RDONLY)

    # Create a new mmap object.
    # size is optional, if not specified the entire file is mapped
    mm = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)

    # Read all the data
    print("%d bytes" % len(mm))
    print("%s" % mm[:])

    # Close the file
    os.close(fd)

    # Close the mmap object
    mm.close()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
