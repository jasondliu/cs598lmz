from bz2 import BZ2Decompressor
BZ2Decompressor.eof = True
from gzip import GzipFile
GzipFile.use_list = True
#from gzip import GzipFile
#GzipFile.extrabuf = 4096
#from gzip import GzipFile
#GzipFile.read = thread.allocate_lock()
from gzip import GzipFile
GzipFile.eof = True
from gzip import GzipFile
GzipFile.extrabuf = 4096
from array import array
array.itemsize = 1
from bz2 import BZ2Compressor
BZ2Compressor.flush = True
from bz2 import BZ2Compressor
BZ2Compressor.compress = True
from bz2 import BZ2Compressor
BZ2Compressor.compress = True
from gzip import GzipFile
GzipFile.myfileobj = None
from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = True
from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = True
from gzip import GzipFile

