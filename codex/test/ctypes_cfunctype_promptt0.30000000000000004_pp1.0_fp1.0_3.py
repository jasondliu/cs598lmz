import ctypes
# Test ctypes.CFUNCTYPE

if __name__ == "__main__":
    import sys
    import os
    import runpy
    import traceback

    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins

    builtins.__NUMPY_SETUP__ = False
    builtins.__CYTHON_SETUP__ = False
    sys.argv[0] = os.path.abspath(sys.argv[0])
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..')))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..', '..', 'Tools')))
