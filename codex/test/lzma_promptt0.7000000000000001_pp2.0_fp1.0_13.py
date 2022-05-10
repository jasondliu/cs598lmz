import lzma
# Test LZMADecompressor with a data stream
# that is supposed to be written to a file.
#
# Note: This test will use a lot of memory, because
# the stream is decompressed into memory before
# writing it to the file.

f = lzma.LZMADecompressor()
with open("test.lzma", "rb") as lzfile:
    data = lzfile.read()

try:
    with open("test.de", "wb") as fd:
        fd.write(f.decompress(data))
    print("File written ok")
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))

print("Done")
