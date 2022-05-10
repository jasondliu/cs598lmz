from lzma import LZMADecompressor
LZMADecompressor().decompress(foo_data)

# +
# Decompress data produced by lzma 1.0+ with lzma 2.0+
from lzma import LZMADecompressor
LZMADecompressor().decompress(foo_data)

from lzma import ( 
    FORMAT_RAW, 
    FORMAT_XZ, 
    check_conservative, 
    check_fast, 
    check_none, 
    filters_from_dict, 
    filters_from_str, 
    filters_to_dict, 
    filters_to_str, 
    FILTER_ARM, 
    FILTER_ARMTHUMB, 
    FILTER_DELTA, 
    FILTER_IA64, 
    FILTER_LZMA1, 
    FILTER_LZMA2, 
    FILTER_POWERPC, 
    FILTER_SPARC, 
    FORMAT_AUTO, 
    FORMAT_ALONE, 
    FORMAT_RAW, 
   
