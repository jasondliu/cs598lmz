import lzma
# Test LZMADecompressor
# decompressor = lzma.LZMADecompressor()
# decompressor.decompress(data)
# decompressor.unused_data

# Test LZMADecompressor
# for chunk in lzma.decompress(data, format=lzma.FORMAT_AUTO, memlimit=2 ** 25, filters=None):
#     print(chunk)

# import gzip
# Test gzip.GzipFile
# Test gzip.decompress
gzip_data = gzip.compress(data)
print("Data length:", len(gzip_data))
print("Uncompressed data length:", len(gzip.decompress(gzip_data)))

# Test gunzip
with open("./out/test.gz", 'wb') as f_out:
    f_out.write(gzip_data)
os.system("gunzip ./out/test.gz")

# Test bz2
bz2_data = bz2.compress(data)
print("Data length:", len(b
