import bz2
# Test BZ2Decompressor

def dstream(decompressor):
    data = b"",
    while True:
        data = data + decompressor.decompress(PART)
        yield data
        data = data.replace(d, b"")
        finished = decompressor.eof                     # qqqqq
        if finished == 1:
            break


decompressor = bz2.BZ2Decompressor()
