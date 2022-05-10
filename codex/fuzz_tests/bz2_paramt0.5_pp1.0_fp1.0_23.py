from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = wrap(BZ2Decompressor.decompress)

from zlib import decompress as zlib_decompress
zlib_decompress = wrap(zlib_decompress)

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    from cPickle import load as cPickle_load
except ImportError:
    from pickle import load as cPickle_load

try:
    from cPickle import loads as cPickle_loads
except ImportError:
    from pickle import loads as cPickle_loads

cPickle_load = wrap(cPickle_load)
cPickle_loads = wrap(cPickle_loads)

try:
    from cPickle import dump as cPickle_dump
except ImportError:
    from pickle import dump as cPickle_dump

cPickle_dump = wrap(cPickle_dump)

try:
    from cPickle import dumps as cPickle_dumps
except ImportError:

