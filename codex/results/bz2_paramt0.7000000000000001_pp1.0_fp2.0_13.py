from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.dumps(b"hello world")) # works

from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b"hello world")) # fails
</code>

