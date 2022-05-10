import _struct

from . import _util
from ._errors import (
    InvalidArgument,
    InvalidKey,
    UnsupportedAlgorithm,
)
from ._util import (
    _verify_key_bytes,
    _verify_signature_bytes,
    _verify_salt_bytes,
)


class _VerifyKey(object):

    _hash_fn = None
    _salt = None
    _verify_key = None

    def __init__(self, verify_key):
        self._verify_key = verify_key

    def verify(self, message, signature, salt=None):
        if not isinstance(message, _bytes_types):
            raise TypeError("message must be bytes")

        if not isinstance(signature, _bytes_types):
            raise TypeError("signature must be bytes")

        if salt is not None:
            if not isinstance(salt, _bytes_types):
                raise TypeError("salt must be bytes")

            if self._salt is not None:
                raise InvalidArgument("salt provided
