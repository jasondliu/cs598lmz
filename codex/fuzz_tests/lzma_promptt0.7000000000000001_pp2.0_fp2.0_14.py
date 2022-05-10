import lzma
# Test LZMADecompressor object

decompressor = lzma.LZMADecompressor()
data = b'lzma compressed data'
decompressor.decompress(data)

# ValueError: this LZMADecompressor object is already used
# decompressor.decompress(data)

# IndexError: data stream has ended
decompressor.decompress(b'')

# ValueError: data stream has ended
decompressor.decompress(b'lzma compressed data')

decompressor.flush()

# ValueError: this LZMADecompressor object is already used
# decompressor.flush()

# IndexError: data stream has ended
decompressor.flush()

decompressor.unused_data
# b''

# ValueError: this LZMADecompressor object is already used
# decompressor.unused_data

# IndexError: data stream has ended
decompressor.unused_data

decompressor.decompress(data)
decompressor.unused_data
# b''


