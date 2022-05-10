import bz2
# Test BZ2Decompressor
data = open('example.txt', 'rb').read()
print(data)

# compression object
compressor = bz2.BZ2Compressor()

# compress data by chunks
for chunk in [data[:4], data[4:8], data[8:12], data[12:]]:
	# compress data and save it to output buffer
	rest = compressor.compress(chunk)
	# if there is data in output buffer, return it as string
	if rest:
		print(rest)

# flush remaining data, if any
rest = compressor.flush()
if rest:
		print(rest)

# Test BZ2Decompressor


# decompression object 
decompressor = bz2.BZ2Decompressor()

# store decompressed data
uncompressed_data = b''

# decompress data by chunks
for chunk in [compressor.compress(data), compressor.flush()]:
	# decompress data and save it to output buffer
	rest = decompressor.decompress(chunk)
	# if there is
