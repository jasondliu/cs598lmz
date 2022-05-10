import weakref

from . import _core
from . import _util
from . import _py3compat

from . import _core
from . import _util
from . import _py3compat

try:
    from . import _cffi_ext
except ImportError:
    _cffi_ext = None

__all__ = [
    'new_allocator', 'new_primitive_type', 'new_pointer_type',
    'new_array_type', 'new_struct_type', 'new_union_type',
    'new_enum_type', 'new_void_type', 'new_function_type',
    'new_c_type', 'new_c_type_with_name',
    'new_c_function_type', 'new_c_function_type_with_name',
    'new_c_function_with_keywords', 'new_c_function_with_keywords_and_name',
    'new_c_function', 'new_c_function_with_name',
    'new_c_function_with_
