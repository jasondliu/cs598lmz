import _structs
from _structs import *
from _structs import __all__ as _structs_all
__all__ = _structs_all

import svn_types
from svn_types import *
from svn_types import __all__ as svn_types_all
__all__.extend(svn_types_all)

# Note: the code in this library typically wont use things like
# svn_error_t, svn_fs_t directly.  Instead, it will do a
# svn.fs._fs_initialize() at the beginning of a public method and
# create a svn.fs.FS object (which will act as a wrapper around the
# _fs_t structure).  It will also grab a pool to use.

from libsvn.auth import *
from libsvn.auth import __all__ as auth_all
__all__.extend(auth_all)
from libsvn.core import *
from libsvn.core import __all__ as core_all
__all__.extend(core_all)
