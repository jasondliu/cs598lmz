import lzma
# Test LZMADecompressor with a known file

with open('test/testdata/blender.xz', 'rb') as f:
    with lzma.LZMADecompressor() as decompressor:
        with open('test/testdata/blender', 'wb') as f2:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                f2.write(decompressor.decompress(chunk))

# Test LZMADecompressor with a known file

with open('test/testdata/blender.xz', 'rb') as f:
    with lzma.LZMADecompressor() as decompressor:
        with open('test/testdata/blender', 'wb') as f2:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                f2.write(decompressor.decompress(chunk))

# Test LZMADecompressor with a known file

with open('test/testdata/blender.xz',
