import weakref

from . import _ffi as ffi
from . import _lib as lib

from ._compat import integer_types, string_types, text_type
from ._compat import int_from_bytes, int_to_bytes
from ._compat import PY2, PY3
from ._compat import xrange

from .errors import (
    AlreadyFinalized,
    BadParameter,
    BufferTooShort,
    InvalidTag,
    LibsodiumError,
    ReadOnly,
)

from .hash import (
    BYTES as HASH_BYTES,
    sha256 as sha256_hash,
    sha512 as sha512_hash,
)

from .random import randombytes

from .stream import (
    STREAM_BYTES_MIN as STREAM_KEY_MIN,
    STREAM_BYTES_MAX as STREAM_KEY_MAX,
    STREAM_NONCEBYTES as STREAM_NONCE_SIZE,
    xchacha20 as xchacha20_stream,
)

from
