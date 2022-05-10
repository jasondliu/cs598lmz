import types
# Test types.FunctionType -- first use a lambda to create a function

f = lambda x,y : x*y

assert type(f) is types.FunctionType

# Now use a function definition

def f(x,y) :
    return x*y

assert type(f) is types.FunctionType

# Now use a class definition

class F(object):
    def __call__(self, x,y) :
        return x*y

f = F()

assert type(f) is types.FunctionType

# Test types.ClassType

assert type(F) is types.ClassType

# Now use a class definition that inherits from object

class F(object):
    def __call__(self, x,y) :
        return x*y

assert type(F) is types.TypeType

# Test types.InstanceType

f = F()
assert type(f) is types.InstanceType

# Test types.NoneType

assert type(None) is types.NoneType

# Test types.NotImplementedType

assert type(
