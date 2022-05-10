import types
# Test types.FunctionType
def func(): pass
assert type(func) == types.FunctionType
# Test types.GeneratorType
def gen(): yield 1
assert type(gen) == types.GeneratorType
assert isinstance(gen(), types.GeneratorType)
# Test types.CodeType
assert type(func.__code__) == types.CodeType
try:
    types.CodeType()
except TypeError:
    pass
else:
    assert False, "Calling CodeType() should fail!"
# Test types.TracebackType
def func2():
    def func3():
        raise Exception
    try:
        func3()
    except:
        return sys.exc_traceback
assert type(func2()) == types.TracebackType
# Test types.ModuleType
assert type(sys) == types.ModuleType
# Test types.InstanceType
class Foo():
    pass
assert type(Foo()) == types.InstanceType
# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType
# Test types.ClassType
assert type(Foo) ==
