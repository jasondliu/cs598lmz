import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/rfc2616.xml.bz2') as src, open('data/rfc2616.xml', 'wb') as dst:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: src.read(100 * 1024), b''):
        dst.write(decompressor.decompress(block))
 
    dst.write(decompressor.flush())
 
# Test BZ2Compressor

with open('data/rfc2616.xml', 'rb') as src, bz2.BZ2File('data/rfc2616.xml.bz2', 'wb') as dst:
    compressor = bz2.BZ2Compressor()
    for block in iter(lambda: src.read(100 * 1024), b''):
        dst.write(compressor.compress(block))
 
    dst.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/rfc26
