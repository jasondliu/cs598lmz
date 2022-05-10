import types
# Test types.FunctionType
def func1(x):
    return x

print(type(func1))
print(type(func1(1)))

# Test types.LambdaType
func2 = lambda x: x

print(type(func2))
print(type(func2(1)))

# Test types.GeneratorType
def func3():
    for i in range(3):
        yield i

print(type(func3))
for i in func3():
    print(type(i))

# Test types.BuiltinFunctionType
print(type(abs))
print(type(abs(-1)))

# Test types.BuiltinMethodType
print(type(list.append))
print(type([].append(1)))

# Test types.MethodType
class A(object):
    def func(self, x):
        return x

a = A()
print(type(a.func))
print(type(a.func(1)))

# Test types.UnboundMethodType
print(type(A.func))
print(type(A.func(a
