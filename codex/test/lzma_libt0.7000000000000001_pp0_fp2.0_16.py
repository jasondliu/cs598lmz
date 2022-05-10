import lzma
lzma.open

#
# patch for lzma
#
if not hasattr(lzma, 'open'):
    def _open(filename, mode):
        if mode.startswith('w'):
            return lzma.LZMAFile(filename, mode)
        else:
            return lzma.LZMAFile(filename, mode, format=lzma.FORMAT_ALONE)
    lzma.open = _open


#
# Python 3.0 - 3.2 compatible code
#
try:
    import cPickle as pickle
except ImportError:
    import pickle


#
# Python 3.0 - 3.2 compatible code
#
try:
    import cStringIO as StringIO
except ImportError:
    import io as StringIO


#
# Python 3.0 - 3.2 compatible code
#
try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen


#
# Patch for Python 3.0 - 3.2
#
