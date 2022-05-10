import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
OUTPUT = 42
"""

import sys

def main():
    if sys.platform == "win32":
        import os
        os.environ["PATH"] = r"C:\Python33;C:\Python33\Scripts;" + os.environ["PATH"]
    from lib_pypy import cffi_backend
    cffi_backend.compile_shared_lib(SRC, VERIFY, OUTPUT)

if __name__ == '__main__':
    main()
