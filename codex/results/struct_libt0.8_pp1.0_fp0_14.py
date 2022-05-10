import _struct
from numba.core.typing.npydecl import parse_signature
from numba.core.errors import TypingError
from numba.core import types

try:
    _ord_char_ndarray = _np.vectorize(ord, otypes=[np.int64])
    _isupper_char_ndarray = _np.vectorize(lambda x: x.isupper(), otypes=[bool])
    _islower_char_ndarray = _np.vectorize(lambda x: x.islower(), otypes=[bool])
    _isspace_char_ndarray = _np.vectorize(lambda x: x.isspace(), otypes=[bool])
    _isdigit_char_ndarray = _np.vectorize(lambda x: x.isdigit(), otypes=[bool])
    _isalpha_char_ndarray = _np.vectorize(lambda x: x.isalpha(), otypes=[bool])
    _isalnum_char_ndarray = _np.vectorize(lambda x: x.isalnum(), otypes=[bool])
    _isident
