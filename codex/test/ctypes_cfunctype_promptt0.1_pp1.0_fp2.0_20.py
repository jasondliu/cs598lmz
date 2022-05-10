import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# The following functions are declared in _ctypes_test.h:
#
# int func(int);
# int func2(int, int);
# int func3(int, int, int);
# int func4(int, int, int, int);
# int func5(int, int, int, int, int);
# int func6(int, int, int, int, int, int);
# int func7(int, int, int, int, int, int, int);
# int func8(int, int, int, int, int, int, int, int);
# int func9(int, int, int, int, int, int, int, int, int);
# int func10(int, int, int, int, int, int, int, int, int, int);
# int func11(int, int, int, int, int, int, int, int, int, int, int);
# int func12(int, int,
