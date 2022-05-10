import ctypes
ctypes.cast(0, ctypes.py_object)

# This is the only way to detect whether the cast
# is necessary.
try:
    ctypes.cast(0, ctypes.py_object)
except TypeError:
    def cast_to_pyobject(x):
        return ctypes.cast(id(x), ctypes.py_object).value
else:
    def cast_to_pyobject(x):
        return x

def is_py3k():
    return sys.version_info >= (3, 0)

def is_pypy():
    return hasattr(sys, 'pypy_version_info')

def is_jython():
    return sys.platform.startswith('java')

def is_win():
    return sys.platform == 'win32'

def is_cygwin():
    return sys.platform == 'cygwin'

def is_cli():
    return sys.platform == 'cli'

def is_ironpython():
    return sys.platform == 'cli'

def is_cpython():

