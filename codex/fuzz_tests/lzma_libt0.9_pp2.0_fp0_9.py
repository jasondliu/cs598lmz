import lzma
lzma_decompress = lzma.decompress
lzma_compress = lzma.compress
MemoryError = MemoryError

_pickle = cPickle

_file = file
_fileopen = _file.__dict__['open']

