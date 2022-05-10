import mmap
import os

def main():
    fsize = os.path.getsize('demo.txt')
    print(fsize)

    # Open the file
    with open('demo.txt', 'r+') as f:
        # memory map the file, size 0 means whole file
        m = mmap.mmap(f.fileno(), 0)

        ###read
        # read content via standard file methods
        print(m.readline())

        # read content via slice notation
        print(m[:5])

        # read content from a specific position
        print(m[2:6])

        ###write
        # write content via standard file methods
        m.write(b'0123456789abcdef')

        # write content via slice notation
        m[5:11] = b'Hello World'

        # update size of map
        m.resize(22)

        # close the map
        m.close()

        # verify
        with open('demo.txt', 'r') as f:
            print(f.read())

