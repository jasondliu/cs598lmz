import ctypes
ctypes.cast(1, ctypes.py_object)

import os, sys
lib_path = os.path.abspath(os.path.join('..', 'utils'))
sys.path.append(lib_path)

