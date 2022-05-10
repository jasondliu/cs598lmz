import mmap
import os
import sys
import time

def main():
    if len(sys.argv) != 3:
        print 'Usage: %s <file> <count>' % sys.argv[0]
        sys.exit(1)

    filename = sys.argv[1]
    count = int(sys.argv[2])

    with open(filename, 'r+') as f:
        mm = mmap.mmap(f.fileno(), 0)
        for i in range(count):
            mm.seek(0)
            mm.write('%d' % i)
            time.sleep(0.1)
        mm.close()

if __name__ == '__main__':
    main()
