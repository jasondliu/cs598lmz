import types
# Test types.FunctionType
def check_types_FunctionType(x):
    if isinstance(x, types.FunctionType):
        return True
    return False

def lab_function(x):
    return x + 1

# Test types.LambdaType
def check_types_LambdaType(x):
    if isinstance(x, types.LambdaType):
        return True
    return False

lab = lambda x : x + 1

# Test types.GeneratorType
def check_types_GeneratorType(x):
    if isinstance(x, types.GeneratorType):
        return True
    return False

def generator():
    for i in range(10):
        yield i

# Test types.GeneratorType
def check_types_GeneratorType(x):
    if isinstance(x, types.GeneratorType):
        return True
    return False

def generator():
    for i in range(10):
        yield i

# Test types.GeneratorType
def check_types_GeneratorType(x):
    if isinstance(x, types
