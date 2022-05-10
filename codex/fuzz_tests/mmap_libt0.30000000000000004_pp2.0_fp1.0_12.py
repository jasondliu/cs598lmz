import mmap
import re
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 {} <file>".format(sys.argv[0]))
        sys.exit(1)
    f = open(sys.argv[1], 'r')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if re.search(br'\x00', s):
        print("Null byte found")
    else:
        print("Null byte not found")
    s.close()
    f.close()

if __name__ == '__main__':
    main()
