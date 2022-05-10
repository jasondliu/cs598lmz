import gc, weakref
from collections import defaultdict
from itertools import chain
from functools import partial

from . import _cffi_backend
from . import _cffi_backend_ctypes
from . import _cffi_backend_internal
from . import _cffi_backend_libffi
from . import _cffi_backend_sysconfigdata
from . import _cffi_errors
from . import _cffi_include
from . import _cffi_utils
from . import _embedding
from . import _pycparser
from . import _verifier
from . import _cdata
from . import _cffi_opcode
from . import _cffi_parse
from . import _cffi_setup
from . import _cffi_types
from . import _cffi_unstub_cache

from . import _cffi_backend_ctypes
from . import _cffi_backend_internal
from . import _cffi_backend_libffi
from . import _cffi_
