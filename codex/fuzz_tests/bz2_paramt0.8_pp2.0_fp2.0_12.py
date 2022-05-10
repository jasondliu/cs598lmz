from bz2 import BZ2Decompressor
BZ2Decompressor()

from pickle import load
import struct
import sys
import time

with BZ2Decompressor() as dec:
    with open('data/trainingData.dat.bz2', 'rb') as f:
        bytes = dec.decompress(f.read())

format = 'i'
offset = 0
num_examples, = struct.unpack_from(format, bytes, offset)
offset += struct.calcsize(format)

width, = struct.unpack_from(format, bytes, offset)
offset += struct.calcsize(format)

height, = struct.unpack_from(format, bytes, offset)
offset += struct.calcsize(format)

format = 'f'

def unpack_image(bytes, index):
    img = []
    for i in range(height):
        start = offset + i * width * struct.calcsize(format)
        end = start + width * struct.calcsize(format)
        img.append(struct.unpack_from(format, bytes, start)[0])
   
