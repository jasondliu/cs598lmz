import types
# Test types.FunctionType
def func():
    pass
print types.FunctionType == type(func)

# Test types.LambdaType
lambda_func = lambda x, y : x+y
print types.LambdaType == type(lambda_func)

# Test types.GeneratorType
def gen():
    for i in range(10):
        yield i
print types.GeneratorType == type((i for i in range(10)))
print types.GeneratorType == type(gen())
