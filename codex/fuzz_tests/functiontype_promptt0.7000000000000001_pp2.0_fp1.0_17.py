import types
# Test types.FunctionType to see if it's callable
if(type(lambda x: x) == types.FunctionType):
    print("lamda is a function")

# Test types.BuiltinFunctionType to see if it's callable
if(type(len) == types.BuiltinFunctionType):
    print("len is a builtin function")

# Test types.MethodType to see if it's callable
if(type(str.lower) == types.MethodType):
    print("str.lower is a method")

# Test types.TypeType to see if it's a class
if(type(str) == types.TypeType):
    print("str is a type")

# Test types.ClassType to see if it's a class
if(type(str) == types.ClassType):
    print("str is a class")

# Test types.InstanceType to see if it's an instance of a class
if(type("") == types.InstanceType):
    print("instance is a type")

# Test types.ModuleType to see if it's a module
if(type(types) == types.
