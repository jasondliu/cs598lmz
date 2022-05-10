import weakref
import types

from ._global_lock import _global_lock
from ._global_lock import _global_lock_dict
from ._global_lock import _global_lock_exceptions
from ._global_lock import _global_lock_list
from ._global_lock import _global_lock_set
from ._global_lock import _global_lock_tuple
from ._global_lock import _global_lock_str
from ._global_lock import _global_lock_bytes
from ._global_lock import _global_lock_bytearray
from ._global_lock import _global_lock_memoryview
from ._global_lock import _global_lock_type
from ._global_lock import _global_lock_weakref
from ._global_lock import _global_lock_weakproxy
from ._global_lock import _global_lock_int
from ._global_lock import _global_lock_float
from ._global_lock import _global_lock_complex
from ._global_lock import _global_lock_bool
