import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(binary_data)

# Decompress data at once
binary_data = bz2.decompress(binary_data)

# Compress and decompress data from file
data = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
file = open("binary_data.bin", "wb")
file.write(data)
file.close()

bz2_file = bz2.BZ2File("binary_data.bin", "rb")
print(bz2_file.read())

bz2_file.close()

# Use bz2 data in memory
file = open("binary_data.bin", "rb")
data = file.read()
#
