import lzma
# Test LZMADecompressor with a file

infile = open("/home/kamal/python/test/test.xz", "rb")
decompressor = lzma.LZMADecompressor()
outfile = open("/home/kamal/python/test/test.txt", "wb")

while True:
    chunk = infile.read(100000)
    if not chunk:
        break
    outfile.write(decompressor.decompress(chunk))

outfile.close()
infile.close()
# Test LZMADecompressor with a file-like object

infile = open("/home/kamal/python/test/test.xz", "rb")
decompressor = lzma.LZMADecompressor()
outfile = open("/home/kamal/python/test/test.txt", "wb")

while True:
    chunk = infile.read(100000)
    if not chunk:
        break
    outfile.write(decompressor.decompress(chunk))


