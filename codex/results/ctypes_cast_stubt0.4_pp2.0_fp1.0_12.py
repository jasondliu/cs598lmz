import ctypes
ctypes.cast(obj, ctypes.py_object).value

# Python 3.x
import sys
sys.getrefcount(obj)

# Python 3.x
import sys
sys.getsizeof(obj)

# Python 3.x
import sys
sys.getsizeof(obj) + sys.getsizeof(obj.__dict__)

# Python 3.x
import sys
sys.getsizeof(obj) + sum(sys.getsizeof(v) for v in obj.__dict__.values())

# Python 3.x
import sys
sys.getsizeof(obj) + sum(sys.getsizeof(v) for v in obj.__dict__.values()) + sum(sys.getsizeof(k) for k in obj.__dict__.keys())

# Python 3.x
import sys
sys.getsizeof(obj) + sum(sys.getsizeof(v) for v in obj.__dict__.values()) + sum(sys.getsizeof(k) for k in obj.__dict__.keys())

# Python 3.x

