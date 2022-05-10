import lzma
# Test LZMADecompressor class

# The test file was created with the command:
#   $ echo test | xz > /tmp/test.xz
#
# It contains a single stream that represents the UTF-8 encoding
# of the string "test".

with open("/tmp/test.xz", "rb") as input:
    decompressor = lzma.LZMADecompressor()
    with decompressor.stream(input) as stream:
        data = stream.read()

print(repr(data))
