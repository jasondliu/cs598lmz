import bz2
# Test BZ2Decompressor
#with open('/home/david/Downloads/example5.bz2', 'rb') as input:
#    decompressor = zstd.ZstdDecompressor()
#    with open('/home/david/Downloads/example5.txt', 'wb') as output:
#        for block in iter(lambda: input.read(1024 * 1024), b''):
#            output.write(decompressor.decompress(block))
#        output.write(decompressor.flush())

#decompressor = zstd.ZstdDecompressor()
#with open('/home/david/Downloads/example5.txt', 'wb') as output:
#    output.write(decompressor.decompress(bz2.BZ2File('/home/david/Downloads/example5.bz2').read()))

# Test ZstdDecompressor
#decompressor = zstd.ZstandardDecompressor()
#with open('/home/david/Downloads/example5.txt', 'wb') as output:
#    output
