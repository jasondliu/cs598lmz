import _struct
# Test _struct.Struct
_struct.Struct('i').format

# Test PyObjC_PyNumberProtocols
_struct.Struct('i').__hash__

# Test PyObjC_InlineSupport
import ctypes
def __NSSwapDouble(x):
    return ctypes.c_double.from_address(id(x))

found_fuzzy = False
try:
    from sys import executable, gettotalrefcount
except:
    print("WARNING: no fuzzy test for pyobjc")
else:

    try:
        import fuzzy
    except ImportError:
        print("fuzzy not found, no fuzzy test for pyobjc")
    else:
        fuzzy.FIXED_INT
        fuzzy.FIXED_LONG
        fuzzy.FIXED_FLOAT
        fuzzy.FIXED_DOUBLE
        fuzzy.FIXED_COMPLEX
        fuzzy.FIXED_OBJECT_ID


        import objc
        fuzzy.test("test_libobjc", objc, verbose=False)
        found_fuzzy = True

if not found_fuzz
