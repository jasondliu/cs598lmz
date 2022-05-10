from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# As a context manager
with BZ2Decompressor() as decompressor:
    decompressor.decompress(bz2_data)

# In a loop
decompressor = BZ2Decompressor()
for chunk in chunks:
    data = decompressor.decompress(chunk)
    if data:
        process(data)
    else:
        break

# With a decompress_buffer() method
decompressor = BZ2Decompressor()
decompressor.decompress_buffer(bz2_data)

# With a decompress_buffer() method and a max_length argument
decompressor = BZ2Decompressor()
decompressor.decompress_buffer(bz2_data, max_length=3)

# With a decompress_buffer() method and a max_length argument
decompressor = BZ2Decompressor()
decompressor.decompress_buffer(bz2_data, max_length=3)

# With a decompress() method and
