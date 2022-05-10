import bz2
# Test BZ2Decompressor

bz2_uncompress_loop = """
def bz2_uncompress_loop(size, data, bz2decompressor):
    bz2decompressor.reset()
    while True:
        chunk = data[:size]
        data = data[size:]
        if not chunk:
            break
        try:
            output = bz2decompressor.decompress(chunk)
        except EOFError:
            if bz2decompressor.eof:
                break
            raise
"""

