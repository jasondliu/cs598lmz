from lzma import LZMADecompressor
LZMADecompressor().decompress(data[3:])

## Using high level libaries

s = "Hello"
s = s.encode('ascii')
s
s = s.decode('ascii')
s
s = s.encode('utf-8')
s
s = s.decode('utf-8')
s
s = s.encode('unicode_escape')
s
s = s.decode('unicode_escape')
s

import logging
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

# pax header
import tarfile
tar = tarfile.open('pax_global_header.tar')
for f in [ 'SOURCES', 'SPECS', 'SRPMS' ]:
    log
