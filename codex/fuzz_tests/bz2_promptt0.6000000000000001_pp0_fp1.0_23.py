import bz2
# Test BZ2Decompressor class with an input file and an output file
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz_decompressor = BZ2Decompressor()

with open('file_to_compress.txt.bz2', 'rb') as input:
    with open('uncompressed.txt', 'wb') as output:
        while True:
            block = input.read(100)
            if not block:
                break
            uncompressed = bz_decompressor.decompress(block)
            if uncompressed:
                output.write(uncompressed)
        # output.write(bz_decompressor.flush())
        uncompressed = bz_decompressor.flush()
        if uncompressed:
            output.write(uncompressed)

#
