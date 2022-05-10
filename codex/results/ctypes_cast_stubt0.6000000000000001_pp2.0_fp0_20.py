import ctypes
ctypes.cast(None, ctypes.py_object)

# This is a workaround for a bug in the 2.6.5 version of py2exe that breaks
# the multiprocessing module.
# http://code.google.com/p/py2exe/issues/detail?id=151
# http://www.py2exe.org/index.cgi/Py2exeAndMultiprocessing
if sys.platform == 'win32' and sys.version_info[:2] == (2, 6):
    ctypes.cast(None, ctypes.py_object)

# py2exe 0.6.9 changed the _Popen object in a way that breaks
# multiprocessing.Process on Windows.
# See http://www.py2exe.org/index.cgi/Py2exeAndMultiprocessing
try:
    from multiprocessing import Process
    import multiprocessing.forking
    if sys.platform == 'win32':
        class _Popen(multiprocessing.forking.Popen):
            def __init__(self, *args,
