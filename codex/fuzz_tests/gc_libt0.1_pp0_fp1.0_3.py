import gc, weakref

from . import _util
from ._util import _get_func_name, _get_func_defaults, _get_func_code, _get_func_globals, _get_func_closure
from ._util import _get_method_function, _get_method_self, _get_method_class
from ._util import _get_class_bases, _get_class_dict, _get_class_name, _get_class_module
from ._util import _get_builtin_type, _get_builtin_object, _get_builtin_method
from ._util import _get_type_bases, _get_type_dict, _get_type_name, _get_type_module
from ._util import _get_object_dict, _get_object_size, _get_object_address
from ._util import _get_frame_locals, _get_frame_globals, _get_frame_code, _get_frame_back
from ._util import _get_traceback_frame, _get_traceback_next
from ._util import _get
