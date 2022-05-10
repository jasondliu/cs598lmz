import mmap
import sys

def main(argv):
    filename = argv[1]
    with open(filename, "r+b") as f:
        # memory-map the file, size 0 means whole file
        mm = mmap.mmap(f.fileno(), 0)
        # read content via standard file methods
        mm.seek(0)
        print "First 10 bytes via read :", mm.read(10)
        print "First 10 bytes via slice:", mm[:10]
        print "2nd   10 bytes via read :", mm.read(10)
        print "2nd   10 bytes via slice:", mm[10:20]
        # close the map
        mm.close()
if __name__ == "__main__":
    main(sys.argv)
