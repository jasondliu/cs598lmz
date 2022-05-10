import weakref

from . import _util
from ._util import _exception_from_status
from ._util import _make_method
from ._util import _register_completion_callback
from ._util import _to_bytes
from ._util import _to_string
from ._util import _validate_output_c_byte_buffer
from ._util import _validate_output_c_string
from ._util import _validate_output_py_bytes
from ._util import _validate_output_py_string
from ._util import _validate_output_py_unicode
from ._util import _validate_output_py_object
from ._util import _validate_output_py_tuple
from ._util import _validate_output_py_dict
from ._util import _validate_output_py_list
from ._util import _validate_output_py_set
from ._util import _validate_output_py_frozenset
from ._util import _validate_output_py_bytearray
from ._util import _validate_output_py_memoryview
