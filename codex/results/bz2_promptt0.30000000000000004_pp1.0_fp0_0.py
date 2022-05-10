import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f_in:
    with open('sample.out', 'wb') as f_out:
        for block in iter(lambda: f_in.read(100 * 1024), b''):
            f_out.write(decompressor.decompress(block))

print(open('sample.out', 'rb').read().decode())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('sample.bz2', 'rb') as f_in:
    with open('sample.out', 'wb') as f_out:
        for block in iter(lambda: f_in.read(100 * 1024), b''):
            f_out.write(compressor.compress(block))
        f_out.write(compressor.flush())

print(open('sample.out', 'rb').read().decode())

# Test BZ2File

with bz2.B
