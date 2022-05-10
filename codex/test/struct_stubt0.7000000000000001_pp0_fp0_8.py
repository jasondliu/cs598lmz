from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('')

s.unpack('')
s.pack('')
s.unpack_from('')
s.pack_into('')

# _ctypes
import _ctypes
from _ctypes import _Pointer
from _ctypes import _SimpleCData, _CData
from _ctypes import _CDataMeta, _CDataMeta, _PointerMeta, _PointerMeta
from _ctypes import sizeof, byref, cast, addressof, POINTER, pointer, CFUNCTYPE
from _ctypes import Structure, Union, Array, _check_size, _copy_from_buffer, _copy_from_buffer_size
from _ctypes import _memmove_addr, _memset_addr
from _ctypes import get_errno, set_errno, get_last_error, set_last_error
from _ctypes import WinError, get_last_error, set_last_error
from _ctypes import create_unicode_buffer, create_string_buffer, wintypes
from _ctypes import _
