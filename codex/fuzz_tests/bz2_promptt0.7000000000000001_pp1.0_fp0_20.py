import bz2
# Test BZ2Decompressor to see if it can decompress the contents of a compressed file.
bz_file = bz2.BZ2File("sample.tar.bz2")
decompressor = bz2.BZ2Decompressor()
for block in iter(lambda: bz_file.read(100 * 1024), b""):
    data = decompressor.decompress(block)
    if data:
        print(data)
 
# Test BZ2Compressor and BZ2Decompressor to see if they can compress and decompress the contents of a file.

with open("sample.tar", 'rb') as input:
    with bz2.BZ2File("sample.tar.bz2", 'wb', compresslevel=9) as output:
        compressor = bz2.BZ2Compressor()
        for block in iter(lambda: input.read(100 * 1024), b""):
            output.write(compressor.compress(block))
        output.write(compressor.flush())
    output.close()
input.close()
 
with open("sample.tar
