import bz2
# Test BZ2Decompressor as a stateless stream filter by decompressing
# individual small chunks of data at a time.

import bz2

inp = b''
outp = b''
