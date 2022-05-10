import ctypes
# Test ctypes.CFUNCTYPE for WIN64 to load these functions
# from this file and call with real pointers and arguments.
# from scipy.weave.inline_tools import is_win64
from numpy.ctypeslib import ndpointer, load_library

# win32_test = is_win64()
win32_test = False

# Turn this on only if win32_test is True
# Copy the C file to the current directory.
# F2PY this file, and then run this test.
# weave_pars = dict(headers=['matrix.h'],
#                   sources=['./c_code.c'],
#                   define_macros=[('F2PY_REPORT_ON_ARRAY_COPY',0), ],
#                   extra_compile_args=['-O'],
#                   tmpdir='./',
#                   relative_paths='.',
#                   )
# weave.inline(c_code.c_code,
#              ['alpha', 'beta', 'gamma'],
#              **weave_pars)

# Turn
