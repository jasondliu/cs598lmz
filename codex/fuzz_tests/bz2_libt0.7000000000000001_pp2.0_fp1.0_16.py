import bz2
bz2.decompress('\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'.decode('hex'))

# or 

from StringIO import StringIO
from bz2 import BZ2Decompressor
bz2decompressor = BZ2Decompressor()
bz2decompressor.decompress('\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'.decode('hex'))

# or

from StringIO import StringIO
from bz2 import BZ2Decompressor
bz2file = StringIO('\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'.decode('hex'))
bz2decompressor = BZ2Decompressor()
bz2decompressor.decompress(bz2file.read())
</code>

