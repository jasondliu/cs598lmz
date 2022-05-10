import bz2
bz2_compressor = bz2.BZ2Compressor()
with bz2.open('compressed_data.bz2', 'wb') as f:
    f.write(bz2_compressor.compress(data))
    f.write(bz2_compressor.flush())
 
compressed_data = open('compressed_data.bz2', 'rb').read()
original_data = bz2.decompress(compressed_data)
len(original_data)

from zlib import compress, decompress, error

compressed_data = compress(data)
original_data = decompress(compressed_data)

len(compressed_data), len(original_data)

compressed_data = compress(data, 9)
original_data = decompress(compressed_data)

len(compressed_data), len(original_data)

decompress(b'z\x9c\xcbH\xcd\xc9\xc9W\x08\xcf/\xcaIQ\xcc \x82
