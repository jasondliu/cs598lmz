import types
# Test types.FunctionType
def func():
    pass

print(type(func))
print(type(func) == types.FunctionType)

# Test types.LambdaType
lambda_func = lambda : None
print(type(lambda_func))
print(type(lambda_func) == types.LambdaType)

# Test types.GeneratorType
gen = (x for x in range(10))
print(type(gen))
print(type(gen) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(sum))
print(type(sum) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type(list.append))
print(type(list.append) == types.BuiltinMethodType)

# Test types.MethodType
class A:
    def method(self):
        pass

print(type(A.method))
print(type(A.method) == types.MethodType)
