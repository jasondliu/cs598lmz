import types
# Test types.FunctionType
def func1():
    pass

print(type(func1) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.MethodType
class Animal(object):
    def run(self):
        print('Animal is running...')

a = Animal()
print(type(a.run) == types.MethodType)

# Test types.UnboundMethodType
print(type(Animal.run) == types.UnboundMethodType)

# Test types.BuiltinMethodType
print(type(len) == types.BuiltinMethodType)

# Test types.ModuleType
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    10 / 0
except:
    print(type(sys.exc_info()[2]) == types.TracebackType)

# Test types.FrameType
def func
