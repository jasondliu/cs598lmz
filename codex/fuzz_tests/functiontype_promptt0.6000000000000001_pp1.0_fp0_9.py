import types
# Test types.FunctionType


def func(a, b):
    return a + b


print(type(func))
print(type(func) is types.FunctionType)
print(type(func) is types.BuiltinFunctionType)
print(type(func) is types.LambdaType)
print(type(func) is types.MethodType)

# Test types.LambdaType

my_lambda = lambda x, y: x + y

print(type(my_lambda))
print(type(my_lambda) is types.LambdaType)
print(type(my_lambda) is types.FunctionType)
print(type(my_lambda) is types.BuiltinFunctionType)
print(type(my_lambda) is types.MethodType)

# Test types.BuiltinFunctionType


class A:
    def __init__(self):
        self.my_list = []

    def append(self, item):
        self.my_list.append(item)

    def __len__(self):
        return len(self.my_list)


a =
