from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# the file is compressed with bz2, and the next level is gzip
# decompress it with bz2 first, then with gzip
import bz2
import gzip
bz2.decompress(gzip.decompress(data))

# the file is compressed with bz2, and the next level is gzip
# decompress it with bz2 first, then with gzip
from bz2 import BZ2Decompressor
from gzip import GzipFile
BZ2Decompressor().decompress(GzipFile(None, 'rb', fileobj=data).read())

# the file is compressed with bz2, and the next level is gzip
# decompress it with bz2 first, then with gzip
import bz2
import gzip
bz2.decompress(gzip.decompress(data))

# the file is compressed with bz2, and the next level is gzip
# decompress it with bz2 first, then with gzip
from bz2 import BZ2Decomp
