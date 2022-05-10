import bz2
bz2.decompress(compressed_data)

# bz2.BZ2Compressor
# bz2.BZ2Decompressor

# bz2.compress(data, compresslevel=9)
# bz2.decompress(data)
# bz2.open(filename, mode='r', compresslevel=9)
# bz2.BZ2File(filename, mode='r', compresslevel=9)

# bz2.compress(data, compresslevel=9)
# bz2.decompress(data)
# bz2.open(filename, mode='r', compresslevel=9)
# bz2.BZ2File(filename, mode='r', compresslevel=9)

from bz2 import BZ2File
bz2_file = BZ2File('sample.bz2', 'w')
bz2_file.write(b'hello world')
bz2_file.close()

bz2_file = BZ2File('sample.bz2', 'r')
bz2
