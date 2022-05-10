import bz2
# Test BZ2Decompressor().decompress()
bz2_decompressor = bz2.BZ2Decompressor()
file_data = open(input_file_path, 'rb').read()
data = bz2_decompressor.decompress(file_data)

# Test bz2.decompress()
#data = bz2.decompress(file_data)

data = data.decode("utf-8")
print(data)
</code>

