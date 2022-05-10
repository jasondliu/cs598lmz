from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.BZ2File(file_in, 'r', 1000000).read()).decode('utf-8')

from bz2 import BZ2Compressor
compress = BZ2Compressor().compress
decompress = BZ2Decompressor().decompress

from json import loads, dumps, load, dump
bool(obj) or None in (obj,)
bools = tuple, bool, numpy.bool_
