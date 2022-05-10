from _struct import Struct
s = Struct.__new__(Struct)
args = (1, 2)
s.pack(*args)

# Test key __getitem__
import sys
from _struct import Struct
s = Struct.__new__(Struct)
args = (1, 2)
sys.modules['_ctypes'] = None
try:
    s.__getitem__(*args)
except ImportError:
    pass

# Test bad nargs for pack_into
import sys
from _struct import Struct
s = Struct.__new__(Struct)
args = (1, 2, 3)
sys.modules['_ctypes'] = None
try:
    s.pack_into(*args)
except ImportError:
    pass

# Test bad key
import sys
from _struct import Struct
s = Struct.__new__(Struct)
args = (1, 2, 3, 5)
sys.modules['_ctypes'] = None
try:
    s.__getitem__(*args)
except (KeyError, ImportError):
    pass

# Test unpack_from nargs
import sys
from _struct import Struct
s =
