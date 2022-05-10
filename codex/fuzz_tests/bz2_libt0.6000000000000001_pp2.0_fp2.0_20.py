import bz2
bz2_compressor = bz2.BZ2Compressor()
print(bz2_compressor.compress(b'We are the champions, my friends, and we'
                              b'keep on fighting til the end.'))

print(bz2_compressor.flush())

print(bz2.decompress(bz2_compressor.compress(b'We are the champions, my friends, and we'
                              b'keep on fighting til the end.')
        + bz2_compressor.flush()))

print(bz2.decompress(bz2.compress(b'We are the champions, my friends, and we'
                              b'keep on fighting til the end.')))

print(bz2_compressor.compress(b''))
print(bz2_compressor.flush())

print(bz2.decompress(bz2_compressor.compress(b'')
        + bz2_compressor.flush()))
