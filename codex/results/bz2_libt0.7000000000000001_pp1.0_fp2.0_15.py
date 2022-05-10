import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# From the command line
# $ bzip2 -c test.py > test.py.bz2
# $ bzip2 -cd test.py.bz2 > test.py

# zlib
import zlib
zlib.compress(b'Hello World!')
zlib.decompress(b'x\234W\300\313H\311\311\311\a\312W(\314K\234\003\000\000\000')

# $ zlib-flate -compress < test.py > test.py.zlib
# $ zlib-flate -uncompress < test.py.zlib > test.py

# gzip
import gzip
from io import BytesIO

buf = BytesIO()
with gzip.GzipFile(mode='wb', fileobj=buf) as fout:
    fout.write(b'Hello World!')
buf.getvalue()

# From the command line
# $ gzip -c test
