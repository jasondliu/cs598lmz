from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = my_decompress
from bz2 import decompress
decompress = my_decompress
#==========================================================================
