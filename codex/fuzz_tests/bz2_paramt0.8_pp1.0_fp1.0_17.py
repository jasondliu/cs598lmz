from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed[8:])

# If you have a file-like object which is compressed and you want to decompress it
# for reading in chunks, one approach is to wrap the file object in a BZ2Decompressor
# instance.
import bz2

uncompressor = bz2.BZ2Decompressor()
with open('lorem.bz2', 'rb') as input:
    with open('lorem.out', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(uncompressor.decompress(block))

# BZ2 files have a built-in integrity check using a CRC-32 checksum.
# If you want to verify the integrity of data coming from an untrusted source,
# the bz2 module can compute the CRC-32 value of the uncompressed data and compare
# it to the value provided in the file.
import bz2

un = bz2.BZ2Decompressor()
un.decompress(b'
