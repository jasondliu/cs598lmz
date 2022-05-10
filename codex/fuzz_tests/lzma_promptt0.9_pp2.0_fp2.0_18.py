import lzma
# Test LZMADecompressor
input_file = "XZ/linux-x64_arm.tar.xz"

file = open(input_file, 'rb')

with file as f:
	dec = lzma.LZMADecompressor()

	print(dec.decompress(f.read()))
print(file.closed)
file.close()


# Test LZMADecompressor.readinto
input_file = "XZ/linux-x64_arm.tar.xz"

with open(input_file, 'rb') as f:
	dec = lzma.LZMADecompressor()

	print(dec.readinto(f))
'''
# Test LZMADecompressor.flush
input_file = "XZ/linux-x64_arm.tar.xz"

with open(input_file, 'rb') as f:
	dec = lzma.LZMADecompressor()

	#print(f.read(4))
	print(dec.flush())
'''



#XZ
