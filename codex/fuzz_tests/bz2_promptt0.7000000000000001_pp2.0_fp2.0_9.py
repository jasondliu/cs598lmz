import bz2
# Test BZ2Decompressor on the 'empty.bz2' file.
with open('empty.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    while True:
        block = f.read(1024)
        if not block:
            break
        decompressor.decompress(block)

# The testfile 'empty.bz2' is empty and thus the decompressor output should be empty.
decompressor.decompress()
decompressor.flush()

# Check that the decompressor's eof property is set.
decompressor.eof == True
