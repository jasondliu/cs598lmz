import mmap
import sys

def main():
    filename = './test.txt'
    f = open(filename, 'r+')
    mm = mmap.mmap(f.fileno(), 0)

    while True:
        mm.seek(0)
        c = mm.readline()
        if c == 'q':
            break
        print "read: %s" % c

    mm.close()
    f.close()

if __name__ == '__main__':
    main()
