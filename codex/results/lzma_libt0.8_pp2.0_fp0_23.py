import lzma
lzma.LZMADecompressor(format=lzma.FORMAT_AUTO, memlimit=None, filters=None)

def unxz(src):
    with open(src, 'rb') as fd:
        decompressor = lzma.LZMADecompressor()
        return decompressor.decompress(fd.read())

with open('cache.bin', 'wb') as fd:
    fd.write(unxz('/Users/daniel/Library/Containers/com.apple.Safari/Data/Library/Caches/Safari/Cache.db.xz'))

import sqlite3
conn = sqlite3.connect('cache.bin')
c = conn.cursor()

for a, b in c.execute('select group_id, url from '
                      'cfurl_cache_response limit 5'):
    print(a, b)
</code>

