import lzma
lzma.decompress(lzma.compress(b'Hello World'))

import zipfile
zf = zipfile.ZipFile('archive.zip', 'w')
