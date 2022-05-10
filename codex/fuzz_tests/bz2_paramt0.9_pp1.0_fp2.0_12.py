from bz2 import BZ2Decompressor
BZ2Decompressor().name = 'bz2'

import tempfile

from . import _cstdio

class File(object):
    def __init__(self, file, mode='r', force_decompressor=None,
                       force_compressor=None):
        self.file = file
        self.mode = mode
        self.force_decompressor = force_decompressor
        self.force_compressor = force_compressor

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        self.file.close()

    def compress(self, compressor=None):
        if self.force_compressor:
            compressor = self.force_compressor
        elif self.mode[0] in 'wxa':
            compressor = 'gzip'  # XXX default should probably be None
        try:
            compressor = _default_compressors[compressor]
        except KeyError:
            raise ValueError('Unsupported compressor: %s' % compressor)

