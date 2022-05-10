import ctypes
ctypes.cast( 0* ctypes.py_object(0), ctypes.py_object ) -> redirect `sys.stderr` stdout to a buffer

import sys, ctypes

def redirect_stdout_stderr(stdout, stderr):
    if sys.platform == 'win32':
        kernel32 = ctypes.windll.kernel32
        kernel32.SetStdHandle(-11, stdout)  # STD_OUTPUT_HANDLE
        kernel32.SetStdHandle(-12, stderr)  # STD_ERROR_HANDLE
```
