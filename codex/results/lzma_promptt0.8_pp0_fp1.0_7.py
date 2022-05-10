import lzma
# Test LZMADecompressor and LZMACompressor by compressing and decompressing
# a text file and comparing the original and decompressed file for equality.

import sys
import timeit
import time
import random

def lzma_decrypt(data):
    with lzma.open(data, mode='rb') as data:
        return data.read()

def lzma_encrypt(data):
    # start = time.clock()
    # print(sys.getsizeof(data))
    with lzma.open(data, mode='wb') as data:
        return data
    # print(sys.getsizeof(data))
    # end = time.clock()
    # print(end - start)

def generate_random_data():
    data = ''
    for i in range(1, 1000000):
        data += ''.join(chr(random.randint(0, 255)) for i in range(10))
    return data

if __name__ == '__main__':
    start = time.clock()
    d = generate_random_data()
    enc
