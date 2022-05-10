import weakref

from . import _pyximport
from . import _pyximport_util
from . import _pyximport_version

# This is the version of the Cython-generated .c file that we expect.
# Bump this whenever the .pyx ABI changes.
ABI_VERSION = _pyximport_version.ABI_VERSION

# The ABI version of the Cython-generated .c file is encoded in the
# filename.  This allows multiple versions to coexist.
#
# The filename format is:
#
#   {modname}-{ABI_VERSION}.{PY_MAJOR}.{extension}
#
# where {modname} is the Python module name, {ABI_VERSION} is the
# ABI_VERSION of this module, {PY_MAJOR} is the major version of Python
# (e.g. "27" or "33"), and {extension} is the usual extension for
# dynamically loaded modules (e.g. "so", "pyd", "dll").

