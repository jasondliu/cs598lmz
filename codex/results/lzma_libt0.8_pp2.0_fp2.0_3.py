import lzma
lzma_methods = [lzma.LZMADecompressor, lzma.LZMACompressor, _lzma.decompress, _lzma.compress]
del lzma
del _lzma

import _json
json_methods = [_json.dump, _json.dumps, _json.load, _json.loads]
del _json

import marshal
import _marshal
marshal_methods = [marshal.dump, marshal.dumps, marshal.load, marshal.loads, _marshal.dump, _marshal.dumps, _marshal.load, _marshal.loads]
del marshal
del _marshal

import _codecs
codecs_methods = [_codecs.open, _codecs.EncodedFile, _codecs.getencoder, _codecs.getdecoder, _codecs.getreader, _codecs.getwriter, _codecs.register, _codecs.lookup]
