import bz2
# Test BZ2Decompressor
data = bz2.BZ2Compressor().compress(b"Hello World!")

d = bz2.BZ2Decompressor()
d.decompress(data)
d.decompress(b"and that's how it went.")

d.flush()
b'Hello World!and that\'s how it went.'

# Test BZ2File

with bz2.open('file.bz2', 'rt') as f:
    file_content = f.read()

with bz2.open('file.bz2', 'wt') as f:
    f.write(file_content)

with bz2.open('file.bz2', 'rt') as f:
    print(f.read(100))

with bz2.open('file.bz2', 'rt') as src, \
        open('file.out', 'wt') as dst:
    dst.write(src.read())
