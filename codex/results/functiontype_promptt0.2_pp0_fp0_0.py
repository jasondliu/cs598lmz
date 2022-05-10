import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
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
def run(self):
    print('Animal is running...')

print(type(run) == types.FunctionType)

# Test types.BuiltinMethodType
print(type(str.lower) == types.BuiltinMethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    print(type(sys.exc_info()[2]) == types.Trace
