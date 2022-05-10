import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as input:
    with open('uncompressed.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
            if not decompressor.eof:
                raise EOFError('Compressed file ended before the '
                               'end-of-stream marker was reached.')
 
# Test BZ2File

with bz2.BZ2File('sample.bz2', 'rb') as input:
    with open('uncompressed.txt', 'wb') as output:
        while True:
            block = input.read(100 * 1024)
            if not block:
                break
            output.write(block)
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('uncompressed.txt', 'rb') as input:
    with open('
