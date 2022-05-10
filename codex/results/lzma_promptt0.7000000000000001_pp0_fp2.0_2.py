import lzma
# Test LZMADecompressor with a file-like object.
with open('foo.xz', 'rb') as f_in, open('foo', 'wb') as f_out:
    decompressor = lzma.LZMADecompressor()
    while True:
        block = f_in.read(1024)
        if not block:
            break
        f_out.write(decompressor.decompress(block))
    f_out.write(decompressor.flush())
