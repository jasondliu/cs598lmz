import ctypes
# Test ctypes.CFUNCTYPE and ctypes.byref

try:
    ffi
except NameError:
    import sys
    if sys.platform == 'win32':
        extra_compile_args = ['-m32']
        extra_link_args = ['-m32']
    else:
        extra_compile_args = ['-fPIC', '-O2']
        extra_link_args = []
