import lzma
# Test LZMADecompressor
with open('test.xz', 'rb') as fh:
    with lzma.LZMADecompressor() as decompressor:
        with open('test.out', 'wb') as outfh:
            for buf in iter(lambda: fh.read(1024 * 1024), b''):
                outfh.write(decompressor.decompress(buf))
            outfh.write(decompressor.flush())
</code>

