import types
# Test types.FunctionType
def function01():
    print("function01")

print(type(function01))

# Test types.LambdaType
lambda01 = lambda: print("lambda01")
print(type(lambda01))

# Test types.GeneratorType
generator01 = (i for i in range(10))
print(type(generator01))


# Test types.MethodType
class A:
    def method01(self):
        print("method01")

a = A()
print(type(a.method01))
print(type(A.method01))

# Test types.BuiltinMethodType
print(type(A.__init__))

# Test types.BuiltinFunctionType
print(type(print))

# Test types.ModuleType
print(type(types))

# Test types.TracebackType
try:
    1/0
except Exception as e:
    print(type(e.__traceback__))

# Test types.FrameType
def function02():
    print("function02")

print(type(function02.__
