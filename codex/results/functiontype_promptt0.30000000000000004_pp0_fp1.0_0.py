import types
# Test types.FunctionType
def func():
    pass

print(type(func))
print(type(func) == types.FunctionType)

# Test types.LambdaType
lam = lambda x: x

print(type(lam))
print(type(lam) == types.LambdaType)

# Test types.GeneratorType
def gen():
    yield 1

print(type(gen))
print(type(gen()) == types.GeneratorType)

# Test types.CodeType
print(type(gen.__code__))
print(type(gen.__code__) == types.CodeType)

# Test types.TracebackType
try:
    1 / 0
except:
    tb = sys.exc_info()[2]

print(type(tb))
print(type(tb) == types.TracebackType)

# Test types.FrameType
def outer():
    def inner():
        return sys._getframe()
    return inner()

print(type(outer()))
print(type(outer()) == types.FrameType)
