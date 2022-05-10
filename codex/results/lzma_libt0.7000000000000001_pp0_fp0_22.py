import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

import base64
import hashlib

import io

import sys
sys.path.append("..")
import lib.config

# NOTE: Do not use this class directly. Use lib.compress.Compress instead.
class Compress(object):
    """This class provides compression methods for the application."""
    def __init__(self):
        super(Compress, self).__init__()
        self.compress_method = lib.config.Config().compress_method

    def compress(self, data):
        """Compresses a given string using the config option."""
        if self.compress_method == "none" or self.compress_method == "":
            return data
        elif self.compress_method == "zlib":
            return zlib_compress(data, 5)
        elif self.compress_method == "lzma":
            return lzma_compress(data)
        elif self.compress
