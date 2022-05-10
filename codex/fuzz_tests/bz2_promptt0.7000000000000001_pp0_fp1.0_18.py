import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('mcpython.bz2', 'rb') as fp:
    file_content = fp.read()
    print("file_content:", file_content)
    decompressed_data = decompressor.decompress(file_content)
    print("decompressed_data:", decompressed_data)
    print("decompressed_data:", type(decompressed_data))
    print("decompressed_data:", len(decompressed_data))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
comp_data = compressor.compress(b'We are the knights who say Ni!')
print("comp_data:", comp_data)
print("comp_data:", type(comp_data))
print("comp_data:", len(comp_data))
comp_data += compressor.flush()
print("comp_data:", comp_data)
print("comp_data:", type(comp_data))
print("comp_data
