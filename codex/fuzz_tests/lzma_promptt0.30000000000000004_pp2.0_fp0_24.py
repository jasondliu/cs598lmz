import lzma
# Test LZMADecompressor

# The data is a binary file of the Python interpreter.
# It is compressed with xz using the default compression settings.

with open("python", "rb") as input, \
     lzma.open("python.xz", "rb") as compressed:
    decompressor = lzma.LZMADecompressor()
    while True:
        block = compressed.read(1024)
        if not block:
            break
        data = decompressor.decompress(block)
        if data:
            input.write(data)
    data = decompressor.flush()
    input.write(data)

# Verify that the output matches the original file.
with open("python", "rb") as f1, open("python.orig", "rb") as f2:
    assert f1.read() == f2.read()
 
# Test LZMADecompressor with multiple streams

# The data is a binary file of the Python interpreter.
# It is compressed with xz using the default compression settings.

with open("python", "rb") as input, \
    
