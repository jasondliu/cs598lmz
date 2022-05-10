from lzma import LZMADecompressor
LZMADecompressor().decompress("scala")

LZMADecompressor()("scala")

# Filters
from lzma import FILTER_X86, FILTER_ARM, FILTER_IA64, FILTER_POWERPC, FILTER_DELTA, FILTER_X86
import os
from lzma import LZMACompressor
os.mkdir("test")
os.chdir("test")
fp = open("foo.xz", 'w')
comp = LZMACompressor(filters=[{
    "id": FILTER_X86,
    "preset": 9
}])
fp.write(comp.compress("scala"))
