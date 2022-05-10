import gc, weakref

from . import _core
from ._core import _get_c_lib_handle
from ._core import _get_c_function
from ._core import _set_c_function
from ._core import _set_c_function_by_name
from ._core import _set_c_function_by_global_name
from ._core import _set_c_function_return_value
from ._core import _set_c_function_exception
from ._core import _get_c_function_exception
from ._core import _get_c_function_return_value
from ._core import _get_c_function_arg
from ._core import _get_c_function_arg_count
from ._core import _get_c_function_arg_type
from ._core import _get_c_function_arg_name
from ._core import _get_c_function_arg_default
from ._core import _get_c_function_arg_is_optional
from ._core import _get_c_function_arg_is_variadic
from ._core import _get_c_function_arg_is
