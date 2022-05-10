from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open(filename, 'rb').read())

# Python 3.4
from bz2 import decompress
decompress(open(filename, 'rb').read())
```
