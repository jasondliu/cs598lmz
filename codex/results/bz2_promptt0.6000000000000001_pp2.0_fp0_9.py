import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# The first decompress call will consume some data, but not all.
# To continue decompressing, call the decompress method again with more compressed data.

decompressor.decompress(compressed_data)

# Once all compressed data has been decompressed, the decompressor object can no longer be used.
# Alternatively, you can use the decompress method until it returns an empty bytes object.

uncompressed_data = b''
while True:
    chunk = decompressor.decompress(compressed_data)
    if chunk == b'':
        break
    uncompressed_data += chunk

# The decompress() method will return an empty bytes object when it reaches the end of the compressed data.
# Once it returns an empty bytes object, the decompressor object can no longer be used.
# It’s possible to decompress data incrementally using decompress(), but the decompress() method requires that the compressed data be passed in correctly.
# The decompress() method will return
