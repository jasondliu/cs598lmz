import types
# Test types.FunctionType is present:
try:
    types.FunctionType
except AttributeError:
    import sys
    print("SKIP")
    sys.exit()

class Test:
    def test(): pass

# __dict__ methods
print(Test.__dict__['test'])
print(Test.__dict__.get('test'))

# import/importlib methods
# (None of them should cause the function object to be recreated)
import test_func
print(test_func.x)
import importlib
importlib.reload(test_func)
