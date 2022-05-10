import types
# Test types.FunctionType for functions
def func():
    pass

print(type(func)==types.FunctionType)
# Test types.LambdaType for lambda functions
x = lambda: None
print(type(x)==types.LambdaType)
# Test types.GeneratorType for generators
def gen():
    yield 1
g = gen()
print(type(g)==types.GeneratorType)



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Functions
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Closures
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# global variable
x = 'global'

def outer():
    # enclosing function
    x = 'enclosing'
    def inner():
        # local variable
        x = 'local'
        print(x)
    inner()

outer()
print
