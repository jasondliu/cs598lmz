import types
# Test types.FunctionType
def func_type_test():
    print("func_type_test")

print(func_type_test())
print(type(func_type_test))
#print(types.FunctionType(func_type_test))

# Test types.LambdaType
lambda_type_test = lambda : print("lambda_type_test")
print(lambda_type_test())
print(type(lambda_type_test))

# Test types.GeneratorType
def generator_test():
    for i in range(4):
        yield i

print(generator_test())

for i in generator_test():
    print(i)

# Test types.MethodType
class class_test():
    def class_test_func():
        print("class_test_func")

print(type(class_test.class_test_func))

# Test types.BuiltinMethodType
print(type(class_test.class_test_func.__call__))

# Test types.MethodDescriptorType
print(type(dict.__dict__['fromkeys
