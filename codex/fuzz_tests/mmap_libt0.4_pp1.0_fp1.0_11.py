import mmap
import sys
import time
import struct

def main():
    # Open the memory mapped file
    fd = os.open(sys.argv[1], os.O_RDONLY)
    mm = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_READ)

    # Read the size of the file
    size = struct.unpack('<L', mm[0:4])[0]

    # Read the data
    data = mm[4:4+size]

    # Print the data
    print(data)

    # Close the memory mapped file
    mm.close()
    os.close(fd)

if __name__ == '__main__':
    main()
