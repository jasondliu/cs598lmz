import _struct

from . import _common
from ._common import _as_bytes, _as_string, _as_unicode, _check_byteslike, _check_unicodelike
from ._common import _check_single_byte_params, _check_single_byte_params_unicode

# --------------------------------------------------------------------
# codec APIs

def register(search_function):
    """register(search_function)

    Register a codec search function. Search functions are expected to take
    one argument, the encoding name in all lower case letters, and return
    a tuple of functions (encoder, decoder, stream_reader, stream_writer)
    (or a single function if the codec doesn't support streams)."""
    if not callable(search_function):
        raise TypeError("argument must be callable")
    _codecs.register(search_function)

def lookup(encoding):
    """lookup(encoding) -> (encoder, decoder, stream_reader, stream_writer)

    Looks up a codec tuple in the Python codec registry and returns
    a tuple of functions.
    """
   
