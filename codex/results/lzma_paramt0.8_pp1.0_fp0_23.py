from lzma import LZMADecompressor
LZMADecompressor()
decompressed_data = decompressor.decompress(compressed_data)
numBytesDecompressed = len(decompressed_data)
print("The number of bytes in the decompressed data is: " + str(numBytesDecompressed))

# Demonstrate that the decompressed data has the same value as the original data
for i in range(0,numBytesOriginal,2):
	if ( decompressed_data[i] != original_data[i] ):
		print("There is a mismatch between the original and decompressed data")
		break
	if ( i >= numBytesOriginal-2 ):
		print("The decompressed data matches the original data")
