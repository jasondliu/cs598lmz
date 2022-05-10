import _struct
import _sys
import _unittest
import _warnings
import _weakref
import __future__
import _collections
import _chunk
import itertools
import _multibytecodec
import _codecs
import _ctypes
import reprlib
import _decimal
import _bisect
import _heapq


_root = _NamespacePath('.', _os.path.dirname(_os.__file__))
import os
import posixpath
import macpath
_namespace_packages = set()

try:
    import nt
except ImportError:
    pass
else:
    import ntpath
    _namespace_packages.add('nt')

try:
    import ce
except ImportError:
    pass
else:
    import ntpath
    _namespace_packages.add('ce')

try:
    import riscospath
except ImportError:
    pass
else:
    _namespace_packages.add('riscos')
try:
    import jospath
except ImportError:
    pass
