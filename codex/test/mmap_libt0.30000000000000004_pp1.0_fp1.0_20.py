import mmap
import struct
import sys

#-------------------------------------------------------------------------------

def usage():
    print("usage: %s <input.bin>" % sys.argv[0])
    sys.exit(1)

#-------------------------------------------------------------------------------

def main():
    if len(sys.argv) != 2:
        usage()

    input_file = sys.argv[1]

    with open(input_file, "rb") as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        while True:
            data = mm.read(4)
            if len(data) != 4:
                break
            (value,) = struct.unpack("<I", data)
            print("0x%08x" % value)

#-------------------------------------------------------------------------------

