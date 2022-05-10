import lzma
lzma.LZMAError

try:
    import bz2
    bz2.BZ2Compressor
except ImportError:
    bz2 = None

import zlib
zlib.MAX_WBITS

try:
    import zstd
    zstd.ZstdDecompressor
except ImportError:
    zstd = None

try:
    import brotli
    brotli.BrotliDecompressor
except ImportError:
    brotli = None

import base64
base64.DEFAULT_ALTCHARS

import binascii
binascii.hexlify

import hashlib
hashlib.md5

import hmac
hmac.HMAC

try:
    import ipaddress
    ipaddress.IPv4Interface
except ImportError:
    ipaddress = None

import itertools
itertools.cycle

import json
json.dumps

import locale
locale.getdefaultlocale

import mailbox
mailbox.Maildir

import math
math.fmod

import
