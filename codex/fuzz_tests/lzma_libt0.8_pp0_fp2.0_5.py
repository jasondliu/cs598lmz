import lzma
lzma = pkgutil.find_loader('lzma')
lzma = lzma and lzma.load_module('lzma')
def _lzma(x): return lzma.compress(x.encode('iso-8859-1'))

bz2 = pkgutil.find_loader('bz2')
bz2 = bz2 and bz2.load_module('bz2')
def _bz2(x): return bz2.compress(x.encode('iso-8859-1'))

import base64
_base64 = lambda x: base64.b64encode(x.encode('iso-8859-1'))

import zlib
_zlib = lambda x: zlib.compress(x.encode('iso-8859-1'))

import snappy
_snappy = lambda x: snappy.compress(x.encode('utf-8'))

_lz4 = lambda x: pylz4.compress(x.encode('utf-8
