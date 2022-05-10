import ctypes
# Test ctypes.CFUNCTYPE
# 
# This test uses a simple C function that returns a pointer to a
# structure.  The structure contains a double and a long, and is
# defined in the C header file 'structs.h'.
# 
# The test checks that the returned structure contains the expected
# values.
# 
# The test also checks that the returned pointer can be used to access
# the structure value.
# 
# The test also checks that the returned pointer can be used to access
# the structure value, and that the value is the same as the value
# returned by the C function.
# 
# The test also checks that the returned pointer can be used to access
# the structure value, and that the value is the same as the value
# returned by the C function.
# 
# The test also checks that the returned pointer can be used to access
# the structure value, and that the value is the same as the value
# returned by the C function.

import support

support.compileJPythonc("test213j.py", core=1, jar="test213.jar",
                        output="test213.
