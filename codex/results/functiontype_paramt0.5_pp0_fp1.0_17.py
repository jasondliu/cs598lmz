from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Issue #16984: __func__ slot
class C:
    def f():
        pass
    f.__func__ is f

# Issue #17072: PyFunction_GetClosure() should return NULL for non-function
# objects.
import _testcapi
_testcapi.PyFunction_GetClosure.__doc__
_testcapi.PyFunction_GetClosure.__doc__ is None
_testcapi.PyFunction_GetClosure(None) is None
_testcapi.PyFunction_GetClosure(1) is None

# Issue #17073: PyFunction_GetCode() should return NULL for non-function
# objects.
_testcapi.PyFunction_GetCode.__doc__
_testcapi.PyFunction_GetCode.__doc__ is None
_testcapi.PyFunction_GetCode(None) is None
_testcapi.PyFunction_GetCode(1) is None

# Issue #17074: PyFunction_GetDefaults() should return NULL for non-function

