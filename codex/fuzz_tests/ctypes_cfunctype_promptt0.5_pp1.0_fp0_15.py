import ctypes
# Test ctypes.CFUNCTYPE
# NOTE: this test requires that the platform has a C compiler installed.
import sys, os
from subprocess import Popen, PIPE
from distutils.spawn import find_executable

def test_cfuntotype_callback():
    '''
    Test that ctypes.CFUNCTYPE(...)(...) works
    '''

    # find a C compiler
    C_compiler = find_executable('cc')
    if C_compiler is None:
        raise RuntimeError("C compiler not found")

    # create a temporary file
    fd, fname = tempfile.mkstemp(suffix='.c')
    os.close(fd)

    # create a C source file
    with open(fname, 'w') as f:
        f.write('#include <stdio.h>\n')
        f.write('#include <stdlib.h>\n')
        f.write('int foo(int (*callback)(int))\n')
        f.write('{\n')
        f.write('    return callback(42);\n')
