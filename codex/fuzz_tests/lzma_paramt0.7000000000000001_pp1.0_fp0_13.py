from lzma import LZMADecompressor
LZMADecompressor.func_code=types.FunctionType(LZMADecompressor.__code__,{})
LZMADecompressor.__module__="lzma"
lzma.LZMADecompressor=LZMADecompressor

from bz2 import BZ2Decompressor
BZ2Decompressor.func_code=types.FunctionType(BZ2Decompressor.__code__,{})
BZ2Decompressor.__module__="bz2"
bz2.BZ2Decompressor=BZ2Decompressor

from zlib import Decompress
Decompress.func_code=types.FunctionType(Decompress.__code__,{})
Decompress.__module__="zlib"
zlib.Decompress=Decompress

from zlib import decompressobj
decompressobj.func_code=types.FunctionType(decompressobj.__code__,{})
decompressobj.__module__="zlib"
zlib.decompressobj=decompressobj

