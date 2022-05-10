import io
# Test io.RawIOBase
from io import RawIOBase
# Test io.BytesIO
try:
    from io import BufferedIOBase
except ImportError:
    BufferedIOBase = object
from io import BytesIO
# Test mmap.mmap
import mmap
# Test pickle
import pickle
# Test pickle's _compat_pickle
from pickle import _compat_pickle
# Test pickletools
import pickletools
# Test reprlib
import reprlib
# Test tempfile
import tempfile
# Test weakref
import weakref
# Test weakref.ref
from weakref import ref
# Test weakref.proxy
from weakref import proxy
# Test weakref.CallableProxyType
from weakref import CallableProxyType
# Test weakref.ProxyType
from weakref import ProxyType
# Test weakref.finalize
from weakref import finalize
# Test weakref.WeakKeyDictionary
from weakref import WeakKeyDictionary
# Test weakref.WeakValueDictionary
from weakref import WeakValueDictionary
# Test winsound
import winsound
# Test xml.
