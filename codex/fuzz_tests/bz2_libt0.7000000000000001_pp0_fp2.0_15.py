import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

from base64 import b64encode, b64decode

from django.utils import simplejson
from django.utils.encoding import smart_unicode
from django.utils.text import compress_string, decompress_string
from django.utils.functional import Promise

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

def _get_encoder_for_compressor(compressor):
    if compressor == 'bz2':
        return bz2_compress
    elif compressor == 'zlib':
        return zlib_compress

def _get_decoder_for_compressor(compressor):
    if compressor == 'bz2':
        return bz2_decompress
    elif compressor == 'zlib':
        return zlib_decompress

def _get_compressor_from_encoding(encoding):
    return encoding.split('-')[
