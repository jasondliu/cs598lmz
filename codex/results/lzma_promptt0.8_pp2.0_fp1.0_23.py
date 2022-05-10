import lzma
# Test LZMADecompressor works
f = open('../data/encoded_data.bin', 'rb')
d = lzma.LZMADecompressor()
print(d.decompress(f.read()))

# Test LZMADecompressor with reading piece by piece 
f = open('../data/encoded_data.bin', 'rb')
d = lzma.LZMADecompressor()

data = f.read(100)

while data:
	decompressed_data = d.decompress(data)
	print(decompressed_data)
	data = f.read(100)
