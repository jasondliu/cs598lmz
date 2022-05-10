import types
# Test types.FunctionType
def func1(x):
    return x

return_value = func1(10)

# Is return_value a function?
print(isinstance(return_value, types.FunctionType))
# Does it take two arguments?
print(func1.__code__.co_argcount == 2)

# And does it return a value?
print(return_value(20) == 20)

# Test types.LambdaType
lambda_return_value = (lambda x : x)(10)

print(isinstance(lambda_return_value, types.LambdaType))
# Does it take two arguments?
print((lambda x : x).__code__.co_argcount == 2)


# Test types.MethodType
class MyClass(object):
    def method1(self, x):
        return x

my_object = MyClass()
my_object_method = my_object.method1

print(isinstance(my_object_method, types.MethodType))
# Does it take two arguments?
print(my_object_method.__code__
