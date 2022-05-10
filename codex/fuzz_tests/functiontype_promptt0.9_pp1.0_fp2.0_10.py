import types
# Test types.FunctionType
ctypes.CFuncPtreType(types.FunctionType(code, globals(), 'f'))() == "Hi"
# FunctionType also throws an OverflowError...

# Test types.BuiltinFunctionType
ctypes.CFuncPtreType(types.BuiltinFunctionType(lambda s: s, globals(), 'l'))() == "Hi"

# Write a C function in a string
TEXT = r"""
#include <stdio.h>
#include <string.h>

const char *str = "Hello";

void f(void)
{
    printf("%s\n", str);
}
"""

# Test ctypes.CDLL and getattr
f = getattr(ctypes.CDLL(util.TESTFN), 'f')
f.restype = None

# Test ctypes.PyDLL
if sys.platform != "win32":
    f = getattr(ctypes.PyDLL, 'f')
    f.restype = None

# Test ctypes._FuncPtr objects
import errno, os
os.
