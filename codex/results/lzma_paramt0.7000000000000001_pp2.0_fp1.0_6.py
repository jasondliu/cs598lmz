from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_compressed)

lzma_compressed

zlib.decompress(zlib_compressed, 15)

zlib_compressed

import bz2
bz2.decompress(bz2_compressed)

bz2_compressed

%%timeit
zlib.decompress(zlib_compressed)

%%timeit
LZMADecompressor().decompress(lzma_compressed)

%%timeit
bz2.decompress(bz2_compressed)

import os
os.getcwd()

os.listdir('../')

import glob
glob.glob('*.py')

import sys
sys.platform

sys.version

sys.path

sys.argv

sys.stdout.write('Hello World\n')

sys.stderr.write('Error')

sys.stdin.readline()

sys.exit()

sys.modules.keys()

import time
time.time()
