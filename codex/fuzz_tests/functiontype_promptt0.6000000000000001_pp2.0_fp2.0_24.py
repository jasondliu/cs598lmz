import types
# Test types.FunctionType

func = lambda x:x
if type(func) != types.FunctionType:
    print("Failed type test on FunctionType")

# Test types.BuiltinFunctionType

def func2(x):
    return x

if type(func2) != types.BuiltinFunctionType:
    print("Failed type test on BuiltinFunctionType")

# Test types.LambdaType

func3 = lambda x:x
if type(func3) != types.LambdaType:
    print("Failed type test on LambdaType")

# Test types.GeneratorType

def generator():
    yield 1

g = generator()
if type(g) != types.GeneratorType:
    print("Failed type test on GeneratorType")

# Test types.GeneratorType

def generator2(x):
    yield x

g2 = generator2(2)
if type(g2) != types.GeneratorType:
    print("Failed type test on GeneratorType")

# Test types.TracebackType

try:
    1/
