import bz2
# Test BZ2Decompressor performance

def decompress(data):
    """
    Returns decompressed `data` payload.
    """
    decompressor = bz2.BZ2Decompressor()
    chunks = []
    while True:
        chunk = decompressor.decompress(data)
        if chunk:
            chunks.append(chunk)
        else:
            break
    return b"".join(chunks)

test_decompress_data = b"test" * 100000

# Test BZ2Compressor performance

def compress(data):
    """
    Returns compressed `data` payload.
    """
    compressor = bz2.BZ2Compressor()
    chunks = []
    while True:
        chunk = compressor.compress(data)
        if chunk:
            chunks.append(chunk)
        else:
            break
    chunks.append(compressor.flush())
    return b"".join(chunks)

test_compress_data = b"testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest
