import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2_decompressor = bz2.BZ2Decompressor()
try:
    decompressed_data = bz2_decompressor.decompress(data)
    print(decompressed_data)
except EOFError:
    print("End of compressed data stream")

# Test BZ2File

print("\n")
bz2_file = bz2.BZ2File("data.bz2")
print(bz2_file.read())
bz2_file.seek(0)
print(bz2_file.read())
bz2_file.close()

# Test Compress

print("\n")
data = b"Hello world!"

