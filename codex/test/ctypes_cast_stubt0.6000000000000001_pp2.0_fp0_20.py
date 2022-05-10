import ctypes
ctypes.cast(None, ctypes.py_object)

# This is a workaround for a bug in the 2.6.5 version of py2exe that breaks
# the multiprocessing module.
# http://code.google.com/p/py2exe/issues/detail?id=151
# http://www.py2exe.org/index.cgi/Py2exeAndMultiprocessing
