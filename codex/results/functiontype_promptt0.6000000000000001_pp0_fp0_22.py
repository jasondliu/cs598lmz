import types
# Test types.FunctionType
def func(x):
    return x

def test_FunctionType():
    assert isinstance(func, types.FunctionType)

class C:
    def m(self):
        return 1

# Test types.MethodType
def test_MethodType():
    assert isinstance(C.m, types.MethodType)
    assert isinstance(C().m, types.MethodType)

# Test types.ClassType, types.InstanceType, types.UnboundMethodType
def test_ClassType():
    class C:
        def m(self):
            return 1
    assert isinstance(C, types.ClassType)
    assert isinstance(C(), types.InstanceType)
    assert isinstance(C.m, types.UnboundMethodType)

# Test types.ModuleType
def test_ModuleType():
    assert isinstance(types, types.ModuleType)

# Test types.TypeType
def test_TypeType():
    assert isinstance(int, types.TypeType)

# Test types.TracebackType
def test_TracebackType():
   
