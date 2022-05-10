import weakref

from . import _cffi_backend
from ._cffi_backend import (
    new_handle, handle_from_ptr, ptr_from_handle,
    handle_from_buffer, buffer_from_handle,
    new_allocator, free_allocator,
    PyObj_FromPtr, PyObj_AsVoidPtr, PyObj_AsVoidPtrAndSize,
    PyObj_FromSigned, PyObj_FromUnsigned,
    Py_TYPE
    )
