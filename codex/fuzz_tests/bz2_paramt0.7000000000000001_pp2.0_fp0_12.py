from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(x)

import cPickle
cPickle.loads(x)

'''

import os
import sys
import struct
import cPickle
import bz2
import shutil

def unpack(data):
    return cPickle.loads(bz2.decompress(data))

def main(in_file, out_file):
    with open(in_file, 'rb') as f:
        data = f.read()
        f.close()
    with open(out_file, 'wb') as f:
        f.write(unpack(data))
        f.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: python %s <in_file> <out_file>" % sys.argv[0]
        sys.exit(0)
    in_file = os.path.abspath(sys.argv[1])
    out_file = os.path.abspath(sys.argv[2])
    if
