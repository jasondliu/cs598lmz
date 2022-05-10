import lzma
lzma_decompress = lzma.decompress

from . import _backend
from . import _templates

from . import _errors
from . import _types


from . import _compat
from ._compat import (
    PY2,
    PY3,
    unichr,
    text_type,
    binary_type,
    unicode_text,
    mbcs_encode,
    mbcs_decode,
    as_bytes,
    as_unicode,
    as_text,
    as_native_str,
    as_native,
    as_unicode_escape,
    as_ascii,
    as_utf8,
    as_latin1,
    as_base64,
    as_hex,
    as_cdata,
    _b,
    _u,
    _as_cdata,
    _int,
    _basestring,
    IS_WIN,
)

from . import _allocate_buffer
from . import _buffers
from . import
