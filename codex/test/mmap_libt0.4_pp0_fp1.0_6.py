import mmap
import struct
import sys

#
#   This is a simple Python script to convert a binary file to an array of bytes.
#   The output is suitable for use as a C array.
#
#   Usage:
#       bin2c.py <binary file>
#
#   Output:
#       The output is written to stdout.
#

def main():
    if len(sys.argv) != 2:
        print('Usage: %s <binary file>' % sys.argv[0])
        return

    with open(sys.argv[1], 'rb') as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        while True:
            data = mm.read(16)
            if len(data) == 0:
                break

            print('    ', end='')
            for b in data:
                print('0x%02x, ' % b, end='')
            print()

        mm.close()

