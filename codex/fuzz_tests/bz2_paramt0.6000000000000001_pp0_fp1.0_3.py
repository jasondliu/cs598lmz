from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = my_decompress

from bz2 import BZ2File
BZ2File.decompress = my_decompress

import bz2
bz2.decompress = my_decompress
 

#from gzip import GzipFile
#GzipFile.decompress = my_decompress
#GzipFile.read = my_read
#GzipFile.__init__ = my_init
#GzipFile.__del__ = my_del

#from gzip import decompress
#decompress = my_decompress

#import gzip
#gzip.decompress = my_decompress
#gzip.GzipFile = GzipFile

class MyCompressor(BZ2Compressor):
    _compress = BZ2Compressor._compress
    _decompress = BZ2Compressor._decompress
    flush = BZ2Compressor.flush
    compress = BZ2Compressor.compress
    decompress = BZ2Compressor.decompress
    __del
