import weakref

from . import _util
from . import _constants
from . import _errors
from . import _objects
from . import _parsers
from . import _types
from . import _wrappers
from . import _functions
from . import _collections
from . import _internal_utils

from . import _api_internal

_api_internal._init_api(globals())

# TODO: This is a hack to make the API work in Python 2.7.
#       We need to remove this once we drop Python 2.7 support.
if sys.version_info < (3,):
    _functions.get_string_array = _functions.get_string_array_py2
    _functions.get_string_array_from_buffer = _functions.get_string_array_from_buffer_py2
    _functions.get_string_array_from_buffer_safe = _functions.get_string_array_from_buffer_safe_py2
    _functions.get_string_array_safe = _functions.get_
