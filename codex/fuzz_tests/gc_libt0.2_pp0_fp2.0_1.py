import gc, weakref

from . import _cffi_backend
from ._cffi_backend import (new_handle, get_handle, get_type_raw,
                            get_exception_raw, get_exception_errno,
                            get_errno, set_errno, newp, cast,
                            callback, gcp, gc_weakref,
                            _num_of_saved_errors, _saved_errors,
                            _get_saved_exception, _get_saved_errno,
                            _get_saved_lib, _get_saved_func,
                            _get_saved_args, _get_saved_result,
                            _get_saved_ffi_errno, _get_saved_ffi_exception,
                            _get_saved_ffi_lib, _get_saved_ffi_func,
                            _get_saved_ffi_args, _get_saved_ffi_result,
                            _get_saved_ffi_back
