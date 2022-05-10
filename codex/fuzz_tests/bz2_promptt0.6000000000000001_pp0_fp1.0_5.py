import bz2
# Test BZ2Decompressor on a file.
source = bz2.BZ2File('README.bz2', 'rb')
dest = open('README.bz2.out', 'wb')

decompressor = bz2.BZ2Decompressor()

while True:
    block = source.read(1024)
    if not block:
        break
    dest.write(decompressor.decompress(block))

dest.close()
source.close()

# Test BZ2Decompressor on a block of data.
data = open('README.bz2', 'rb').read()
decompressor = bz2.BZ2Decompressor()
plain_data = decompressor.decompress(data)
plain_data += decompressor.flush()
assert plain_data == open('README', 'rb').read()
