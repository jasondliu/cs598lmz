from types import FunctionType
list(FunctionType(f.__code__, {}).__globals__)
# output: ['__builtins__', '__name__', '__doc__', '__package__']

def f():
    pass

# output: ['__builtins__', '__name__', '__doc__', '__package__']
list(f.__globals__)
</code>

