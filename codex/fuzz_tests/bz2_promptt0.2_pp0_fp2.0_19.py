import bz2
# Test BZ2Decompressor

with open('data/sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(block)
        if data:
            print(data)

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
with open('data/sample.bz2', 'rb') as f_in, \
        open('data/sample.copy.bz2', 'wb') as f_out:
    while True:
        block = f_in.read(1024)
        if not block:
            break
        out = compressor.compress(block)
        if out:
            f_out.write(out)
    out = compressor.flush()
    f
