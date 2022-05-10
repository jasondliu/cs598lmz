import bz2
bz2.decompress(bz2.compress('this is a test'))

# Python 2.6.6
import bz2
bz2.BZ2Decompressor().decompress(bz2.BZ2Compressor().compress('this is a test'))

# Python 2.6.6
import bz2
c = bz2.BZ2Compressor()
print c.compress('this is a test')
print c.flush()
d = bz2.BZ2Decompressor()
print d.decompress(bz2.compress('this is a test'))
print d.flush()

# Python 2.6.6
import bz2
print bz2.compress('this is a test')
print bz2.decompress(bz2.compress('this is a test'))

# Python 2.6.6
import bz2
print bz2.decompress(bz2.compress('this is a test'))

# Python 2.6.6
import bz2
