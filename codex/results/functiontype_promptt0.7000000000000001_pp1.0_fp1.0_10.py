import types
# Test types.FunctionType
def func():
    return 1
print(type(func))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in range(10))))
print(type(x for x in range(10)))
print(type(1))

print(type([]))
print(type(()))
print(type({}))


print(type(dict))

print(type(str))
print(type(bool))

print(type(int))

print(type(None))

# Test types.GeneratorType
def g():
    yield 1

print(type(g))
print(type(g()))

# Test types.BuiltinFunctionType
print(type(abs))

# Test types.LambdaType
print(type(lambda x: x))

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    print(type(sys.exc_info()[2]))

# Test class
class A:
    pass

a = A()

