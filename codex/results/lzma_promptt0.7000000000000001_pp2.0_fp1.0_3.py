import lzma
# Test LZMADecompressor with a single-byte buffered LZMAFile.

def test_read1(size, data):
    f = io.BytesIO(data)
    lz = lzma.LZMADecompressor()
    bufsize = 1
    with lzma.LZMAFile(f, mode='r', buffered=True, bufsize=bufsize) as xf:
        chunks = []
        while True:
            chunk = xf.read(size)
            if not chunk:
                break
            chunks.append(chunk)
    return b''.join(chunks)
# Test LZMADecompressor with a multi-byte buffered LZMAFile.

def test_read2(size, data):
    f = io.BytesIO(data)
    lz = lzma.LZMADecompressor()
    bufsize = 4
    with lzma.LZMAFile(f, mode='r', buffered=True, bufsize=bufsize) as xf:
        chunks = []
        while True:
            chunk = x
