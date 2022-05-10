import types
# Test types.FunctionType, since this is just used to test the above.
if "FunctionType" not in types.__dict__:
    raise ImportError("Can't find types.FunctionType.")
def tempfunc():
    pass
if type(tempfunc) != types.FunctionType:
    raise ImportError("types.FunctionType doesn't work.")


# Import the whole test suite.
import cpmodule
