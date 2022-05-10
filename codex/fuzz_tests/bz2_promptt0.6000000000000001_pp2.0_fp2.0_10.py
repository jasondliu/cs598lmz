import bz2
# Test BZ2Decompressor
bz2dec = bz2.BZ2Decompressor()
x = bz2dec.decompress(compressed_data)
x == data

# Test BZ2Compressor
bz2comp = bz2.BZ2Compressor()
x = bz2comp.compress(data)
x == compressed_data

x += bz2comp.flush()
x == compressed_data

# Test bz2.compress() and bz2.decompress()
x = bz2.compress(data)
x == compressed_data

x = bz2.decompress(compressed_data)
x == data

# Test open()
with bz2.open(BytesIO(compressed_data), mode="rb") as fo:
    x = fo.read()
x == data

with bz2.open(BytesIO(data), mode="wb") as fo:
    x = fo.write(data)
x == len(data)

with bz2.open(BytesIO(compressed_data), mode="
