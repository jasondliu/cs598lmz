from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# %%

from lzma import open
with open('/tmp/backup.tar.xz', 'rt') as f:
    print(f.read())

# %%

from lzma import open
with open('/tmp/backup.tar.xz', 'wt', preset=9 | lzma.PRESET_EXTREME) as f:
    f.write('main()')

# %%

from lzma import open
with open('/tmp/backup.tar.xz', 'rb') as f:
    data = f.read()
with open('/tmp/backup.tar', 'wb') as f:
    f.write(data)

# %%

import zlib
s = b'witch which has which witches wrist watch'
len(s)

# %%

t = zlib.compress(s)
len(t)

# %%

zlib.decompress(t)

# %%

zlib.crc32(s)


