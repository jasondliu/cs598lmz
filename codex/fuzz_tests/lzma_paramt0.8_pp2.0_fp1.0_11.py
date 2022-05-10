from lzma import LZMADecompressor
LZMADecompressor.decompress(data)
print("done decompressing")
# print("done decompressing")
# data = gzip.GzipFile(fileobj=data, mode="rb")
# print("done decompressing")
# data = zlib.decompress(data)
# print("done decompressing")
# data = data.decode("utf-8")
# print("done decompressing")
data.decode("utf-8")
print("done decompressing")

# writing the data to a file
with open("output.txt", "w") as f:
    f.write(data)
