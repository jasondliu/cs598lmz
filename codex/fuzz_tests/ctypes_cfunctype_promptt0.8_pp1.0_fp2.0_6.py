import ctypes
# Test ctypes.CFUNCTYPE's ability to call a C function with a non-null-terminated string.
lib = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), 'ctypes_test.so'))
my_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int)(('my_func', lib))
assert my_func(b'my string', 11) == 3
# Test how ctypes.CDLL handles the case where the OS wants us to initialize a library
# with a C function that it can call later to shut down.
lib = cdll.LoadLibrary(os.path.join(os.path.dirname(__file__), 'init_finalize_test.so'))
lib.bar(7)
# Test that ctypes.CDLL handles a library that declares a constructor but doesn't
# declare a destructor, and vice versa.
import os
if os.name == 'nt':
  sys.exit(0) # Don't test this on Windows yet
lib_constructor_
