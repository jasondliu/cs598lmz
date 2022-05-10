import bz2
bz2_compressor = bz2.BZ2Compressor()
data = b'{"name": "Foo", "foo": "bar"}'
data += b'{"name": "Baz", "foo": "qux"}' * 100000
compressed_data = bz2_compressor.compress(data)
compressed_data += bz2_compressor.flush()
len(data)

len(compressed_data)

decompressor = bz2.BZ2Decompressor()
original_data = decompressor.decompress(compressed_data)
original_data

original_data == data

with bz2.open(filename, mode="wt") as dst:
    dst.write(data.decode("utf-8"))

with bz2.open(filename, mode="rt") as src:
    restored_data = src.read()
restored_data == data.decode("utf-8")

data = b'{"name": "Foo", "foo": "bar"}'
data += b'{"name": "Baz
