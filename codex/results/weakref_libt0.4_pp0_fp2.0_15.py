import weakref

from . import utils
from .. import _ffi
from .. import _lib
from .. import _utils
from .. import _enums
from .._enums import (
    _Direction,
    _MemoryAccess,
    _MemoryFlags,
    _MemoryType,
    _MemcpyKind,
    _MemcpyDirection,
    _MemsetKind,
    _MemsetPattern,
    _MemsetPatternKind,
    _MemsetPatternType,
    _MemsetPatternSize,
)
from .._errors import get_el_error_code, get_el_error_message

from .buffer import Buffer
from .context import Context
from .device import Device
from .image import Image
from .platform import Platform
from .queue import Queue


class Memory:
    """
    OpenCL memory object.

    Args:
        context: The context in which the memory object is created.
        flags: A bit-field that is used to specify allocation and usage information
            about the memory object being created.
        host_ptr: A pointer to the buffer in host memory
