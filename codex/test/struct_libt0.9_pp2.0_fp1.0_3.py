import _struct
import _sha1

from _sha1 import *

_sha = _sha1._sha1
blocksize = 1        # legacy value (wrong, but true in Python 1.5.2)


class sha(object):
    digest_size = 20
    _h0 = 0x67452301
    _h1 = 0xefcdab89
    _h2 = 0x98badcfe
    _h3 = 0x10325476
    _h4 = 0xc3d2e1f0

    def __init__(self, s=None):
        self._buffer = b''
        self._count = 0

        # deprecated variable allowing use of the "old" interface
        self._legacy_api = False

        if s:
            self.update(s)

    def update(self, s):
        if not isinstance(s, bytes):
            raise TypeError("object supporting the buffer API is required")

        if self._legacy_api:
            tmp = self._buffer + (s,)
