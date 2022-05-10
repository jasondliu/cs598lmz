import lzma
lzma = lzma.LZMAFile('/home/ubuntu/scratch/test_data/test_file.lzma', mode='w')
lzma.write(user_data.encode())
lzma.close()

import bz2
bz2 = bz2.BZ2File('/home/ubuntu/scratch/test_data/test_file.bz2', mode='w')
bz2.write(user_data.encode())
bz2.close()

import zlib
zlib = zlib.compressobj(1)
with open('/home/ubuntu/scratch/test_data/test_file.z', 'wb') as compress_file:
     compress_file.write(zlib.compress(user_data.encode()))
     compress_file.write(zlib.flush())

import brotli
with open('/home/ubuntu/scratch/test_data/test_file.br', 'wb') as compress_file:
     compress_file.write(brotli.compress(
