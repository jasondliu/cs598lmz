import types
# Test types.FunctionType
def my_add(a,b):
    return a+b
print isinstance(my_add,types.FunctionType)

# Test types.LambdaType
my_add = lambda a,b : a+b
print isinstance(my_add,types.LambdaType)

# Test types.CodesType
print isinstance(my_add.func_code,types.CodeType)

# Test types.GeneratorType
def gen_fun():
    for i in range(5):
        yield i*i
print isinstance(gen_fun(),types.GeneratorType)
print gen_fun()
print gen_fun()
print gen_fun()
print gen_fun()
