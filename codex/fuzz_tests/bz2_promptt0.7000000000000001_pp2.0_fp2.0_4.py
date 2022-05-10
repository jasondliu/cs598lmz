import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
d.decompress(compressed)

# Test BZ2File
with bz2.BZ2File(file=io.BytesIO(compressed)) as f:
    text = f.read().decode()

# Test BZ2File with block size
d = bz2.BZ2Decompressor()
with bz2.BZ2File(file=io.BytesIO(compressed), mode='r', compresslevel=9) as f:
    f.seek(0)
    while True:
        block = f.read(1024 * 1024)
        if not block:
            break
        text += d.decompress(block)

# Test BZ2File with seek
with bz2.BZ2File(file=io.BytesIO(compressed), mode='r', compresslevel=9) as f:
    f.seek(0)
    text = f.read().decode()

# Test BufferedReader
with bz2.BZ2File(file=io.Bytes
