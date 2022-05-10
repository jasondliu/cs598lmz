import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

import sys
import os

from .codes import *

try:
    import ctypes
    if sys.platform == 'win32':
        _libcrypt32 = ctypes.windll.crypt32
        _win32cryptcon = getattr(ctypes, 'WIN32_CERT_CONTEXT', ctypes.c_void_p)
    else:
        _libcrypt32 = None
        _win32cryptcon = None
except ImportError:
    _libcrypt32 = None
    _win32cryptcon = None


_cached_certs = {}
_cached_keyids = {}


def _load_ms_pkcs7(data):
    global _win32cryptcon, _libcrypt32, _cached_certs, _cached_keyids
    cdata = None
    cert_contexts = []
    key_ids = []
    if _win32cryptcon is not None:
        cdata = ctypes.create_string_buffer(data, len(data))
        pdata
