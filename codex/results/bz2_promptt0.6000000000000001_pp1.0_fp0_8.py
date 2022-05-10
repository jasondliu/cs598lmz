import bz2
# Test BZ2Decompressor
#

import bz2

decomp = bz2.BZ2Decompressor()

try:
    decomp.decompress(b"blah")
except ValueError:
    print("OK")

try:
    decomp.decompress(b"BZh9")
except ValueError:
    print("OK")

try:
    decomp.decompress(b"BZh9ar")
except ValueError:
    print("OK")

try:
    decomp.decompress(b"BZh9ar1")
except ValueError:
    print("OK")

try:
    decomp.decompress(b"BZh9ar12")
except ValueError:
    print("OK")

try:
    decomp.decompress(b"BZh9ar12p")
except ValueError:
    print("OK")

try:
    decomp.decompress(b"BZh9ar12p1")
except ValueError:
    print("OK")

try:
    decomp.decompress(
