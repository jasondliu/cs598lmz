import _struct
import traceback
import ctypes
import ctypes.wintypes

from ctypes import c_int, c_uint, c_ulong, c_longlong, c_char_p

from typing import Iterable, Tuple, Union

from . import get_debug_privilege, is_64bit, is_windows



# Thanks to mrexodia for this code
def _get_module_base(pid: int, name: str) -> int:
    """
    Gets the base address of the given module in the given process

    :param pid: The process id to look for the module in
    :param name: The name of the module
    :return: The module base address
    """
    peb = _ctypes.c_longlong()
    k32 = _ctypes.windll.kernel32
    k32.ReadProcessMemory.restype = _ctypes.wintypes.BOOL
