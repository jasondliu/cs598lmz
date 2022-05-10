import lzma
lzma.LZMAFile

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0], file=sys.stderr)
        return 1

    for filename in sys.argv[1:]:
        if not os.path.exists(filename):
            print("%s does not exist" % filename, file=sys.stderr)
            return 1

    for filename in sys.argv[1:]:
        with open(filename, 'rb') as f:
            file_size = os.path.getsize(filename)
            data = f.read(file_size)
            # print(data)
            data = lzma.decompress(data)
            # print(data)
            data = data.decode('utf-8')
            # data = data.decode('ascii')
            # print(data)
            print(data, end='')

if __name__ == '__main__
