from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# The decompress() method can be fed arbitrary bytes and it will return
# the uncompressed version of more and more of the data each time you call it.

# The decompress() method will return an empty bytes object when it has
# consumed all of the compressed data.

with open('lorem.txt.bz2', 'rb') as input:
    decompressor = BZ2Decompressor()
    with open('lorem.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
