import types
# Test types.FunctionType
def func(x):
    return x

print type(func)
print type(func(1))
print type(lambda x: x)
print type(lambda x: x)(1)

# Test types.LambdaType
print type(lambda x: x)
print type(lambda x: x)(1)

# Test types.GeneratorType
def gen():
    yield 1

print type(gen)
print type(gen())

# Test types.ClassType
class cls:
    pass

print type(cls)
print type(cls())

# Test types.InstanceType
class cls:
    pass

print type(cls())

# Test types.MethodType
class cls:
    def meth(self):
        pass

print type(cls.meth)
print type(cls().meth)

# Test types.UnboundMethodType
class cls:
    def meth(self):
        pass

print type(cls.meth)

# Test types.BuiltinFunctionType
print type(len
