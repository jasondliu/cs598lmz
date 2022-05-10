import mmap
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <file>" % sys.argv[0])
        sys.exit(1)

    f = open(sys.argv[1], "r+b")
    mm = mmap.mmap(f.fileno(), 0)
    mm.seek(0)
    mm.write(b"\x00")
    mm.close()
    f.close()

if __name__ == "__main__":
    main()
