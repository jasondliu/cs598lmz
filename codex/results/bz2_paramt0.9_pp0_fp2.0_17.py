from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data_compressed)

if data_compressed == bz2.compress(data):
    print "Equal!"
else:
    print "Unequal!"


print len(lzma.compress(data))
print len(bz2.compress(data))
print len(zlib.compress(data))

print lzma.decompress(lzma.compress(data)) == data
print bz2.decompress(bz2.compress(data)) == data
print zlib.decompress(zlib.compress(data)) == data

from lzma import LZMADecompressor
from mmseg import mmseg
from bz2 import BZ2Decompressor
from zlib import Decompress
from mmseg import seg_txt, seg_txt_to_dict
import timeit

benchmarks = {
    "mmseg": {
        "import": True,
        "prep_code": "from mmseg import seg_txt, seg_txt_
