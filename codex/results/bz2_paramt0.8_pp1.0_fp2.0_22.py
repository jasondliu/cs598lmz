from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(BZ2_data)

#pkpy
import pickle
# pickle.loads(serialized_data)
# pickle.dumps(data)

#gzip
import gzip
# gzip.compress(data)
# gzip.decompress(gzipped_data)
with gzip.open('myfile.gz', mode='wt', compresslevel=5) as f:
    f.write(uncompressed_data)
with gzip.open('myfile.gz', mode='rt') as f:
    text = f.read()

#brotli
import brotli
# brotli.compress(data)
# brotli.decompress(compressed_data)

#lzma
# import lzma
# lzma.compress(data)
# lzma.decompress(compressed_data)

#lz4
import lz4.frame
# lz4.frame.compress(data)
# lz4.frame.decompress(compressed_data
