import ctypes
# Test ctypes.CFUNCTYPE
restype = ctypes.c_char_p
argtypes = ctypes.c_char_p
cfunc = ctypes.CFUNCTYPE(restype, argtypes)(6681278)
cfunc.__doc__ = 'Fossil'
cfunc(b'Sinclair')

# Test ctypes.CDLL
import tempfile, os
# Create a temporary C source file
tempCfile = tempfile.NamedTemporaryFile(suffix='.c', delete=False)
libname = os.path.split(tempCfile.name)[1][:-2]
with open(tempCfile.name, 'w') as f:
    f.write(
        '#include <stdio.h>\n' +
        'void hello(const char *name) { printf("Hello %s!\\n", name); }\n'
    )
# Create DLL
import subprocess, ctypes
