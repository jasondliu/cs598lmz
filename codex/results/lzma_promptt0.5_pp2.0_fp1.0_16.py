import lzma
# Test LZMADecompressor with a file-like object.
with open('lzma_compressed', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with open('lzma_uncompressed', 'wb') as fout:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            data = decompressor.decompress(chunk)
            if data:
                fout.write(data)
        fout.write(decompressor.flush())
</code>

