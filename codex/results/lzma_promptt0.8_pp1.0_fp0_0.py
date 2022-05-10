import lzma
# Test LZMADecompressor on a simple string.
compressor = lzma.LZMACompressor()
compressor.compress(b'begin ')
compressor.flush()
assert compressor.unused_data == b''
print(compressor.compress(b'end.'))
compressor.flush()
print(compressor.unused_data)


import tarfile
# Test tarfile compression options
with tarfile.open('foo.tar', mode='w') as tf:
    tf.add('README.txt', compress_type=tarfile.COMPRESSION_BZIP2)
    tf.add('README.txt', compress_type=tarfile.COMPRESSION_XZ)
    tf.add('README.txt', compress_type=tarfile.COMPRESSION_LZMA)
    with open('README.txt', mode='rb') as fo:
        tf.addfile(tarfile.TarInfo('README2.txt'), fo)
# ...and extract it.
with tarfile.open('foo.tar', mode='r') as tf:
    for ti in tf
