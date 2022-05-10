from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# or use the bz2 module
import bz2
bz2.decompress(data)

# or use the bz2file module
import bz2file
bz2file.BZ2File(filename).read()
</code>

