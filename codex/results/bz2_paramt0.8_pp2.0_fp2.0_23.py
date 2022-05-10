from bz2 import BZ2Decompressor
BZ2Decompressor

decompressor = BZ2Decompressor()
data = decompressor.decompress(compressed_data)
data

compressed_data[:4]

len(data), len(compressed_data)

import bz2
bz2.BZ2File('data.txt.bz2')

import shutil
shutil.unpack_archive('hello.zip')
