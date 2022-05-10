import types
# Test types.FunctionType

def test_function_type():
    assert type(f1)==types.FunctionType
    assert type(f2)==types.FunctionType
    assert type(f3)==types.FunctionType

def f1(x,y):
    return x*y

def f2(x,y):
    return x*y

class c:
    def f3(self,x,y):
        return x*y

# Test types.InstanceType

def test_instance_type():
    assert type(f1.__closure__[0])==types.CellType
    assert type(f2.__closure__[0])==types.CellType
    assert type(f3)==types.FunctionType

def test_function_type_repr():
    assert repr(f1) == "<function f1 at %x>" % (id(f1),)

def test_function_type_doc():
    assert f1.__doc__ == None

def test_function_dir_inherited():
    assert '__call__' in dir(f
