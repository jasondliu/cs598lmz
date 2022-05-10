import bz2
# Test BZ2Decompressor with read()

with bz2.BZ2File(TESTFN, 'rb') as bz2src, \
        bz2.BZ2Decompressor() as d:
    read_chunks = [d.read(5) for _ in range(30)]
    bz2src.seek(0)
    src_chunks = [bz2src.read(5) for _ in range(30)]
    for read_chunk, src_chunk in zip(read_chunks, src_chunks):
        assert read_chunk == src_chunk

# Test BZ2Decompressor with readinto()
with bz2.BZ2File(TESTFN, 'rb') as bz2src, \
        bz2.BZ2Decompressor() as d:
    bz2src.seek(0)
    src = bz2src.read()

    buf_len = 20
    buf = bytearray(buf_len)
    buf_left = len(buf)

    while buf_left:
        buf_
