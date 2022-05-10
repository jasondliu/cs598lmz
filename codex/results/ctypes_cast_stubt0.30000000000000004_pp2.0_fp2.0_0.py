import ctypes
ctypes.cast(None, ctypes.py_object)

# This is a workaround for a bug in multiprocessing/heap.py
# See http://bugs.python.org/issue9400 for more information
# Without this workaround, you'll see a RuntimeError:
#    RuntimeError: SynchronizedArray objects should only be shared between processes through inheritance
import multiprocessing.heap
multiprocessing.heap.SynchronizedArray = multiprocessing.Array

# This is a workaround for a bug in multiprocessing/util.py
# See http://bugs.python.org/issue6721 for more information
# Without this workaround, you'll see a RuntimeError:
#    RuntimeError: Queue objects should only be shared between processes through inheritance
import multiprocessing.util
multiprocessing.util._finalizer_registry.clear()

# This is a workaround for a bug in multiprocessing/managers.py
# See http://bugs.python.org/issue14306 for more information
# Without this workaround, you'll see a RuntimeError:
#    RuntimeError:
