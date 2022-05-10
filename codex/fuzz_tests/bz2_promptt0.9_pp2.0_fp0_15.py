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

exec bz2_uncompress_loop
exec bz2_uncompress_loop.replace('try:', '''try:
            output = save('bz2decompressor', output)''')
def count_output(bz2decompressor):
    return len(save('bz2decompressor', bz2decompressor.decompress()))
counts = {
    1024: 1106779,
    2048: 1106779,
    4096: 1106779,
    8192: 1106779,

