import lzma
lzma.decompress(lzma.compress(b'Hello'))

#%% lzma.open()
# lzma.open(filename, mode='r', format=FORMAT_AUTO, check=-1, preset=None, filters=None, encoding=None, errors=None)
# mode: r, w, x, a, r+, w+, x+, a+,
# format: FORMAT_AUTO, FORMAT_XZ, FORMAT_ALONE, FORMAT_RAW
# check: CHECK_NONE, CHECK_CRC32, CHECK_CRC64, CHECK_SHA256
# preset: 0-9, None (default)
# filters: None, list of dict
# encoding: None, encoding name (e.g. 'utf-8')
# errors: None, 'strict', 'ignore', 'replace'

with lzma.open('foo.xz', 'wt') as f:
    f.write('Hello world!')

