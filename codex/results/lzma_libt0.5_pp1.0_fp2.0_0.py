import lzma
lzma.LZMAError

# ---

try:
	import bz2
	bz2.BZ2Error
except ImportError:
	bz2 = None

# ---

try:
	import gzip
	gzip.GzipFile
except ImportError:
	gzip = None

# ---

try:
	import zlib
	zlib.ZlibError
except ImportError:
	zlib = None

# ---

try:
	import snappy
	snappy.UncompressError
except ImportError:
	snappy = None

# ---

try:
	import lz4
	lz4.LZ4Error
except ImportError:
	lz4 = None

# ---

try:
	import lzf
	lzf.LZFError
except ImportError:
	lzf = None

# ---

try:
	import lzw
	lzw.LZWFile
except ImportError:
	lzw = None

# ---

try:
