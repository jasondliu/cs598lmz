from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo").__closure__)

# This is a bit different.  It's the same function, but __closure__ is
# empty.  This is because the closure is empty.

def f():
    return

f.__closure__

# This is a function that returns a function that uses a closure.

def f():
    x = [1,2,3]
    def g():
        return x
    return g

g = f()
g.__closure__

# This is a function that returns a function that uses a closure.

def f():
    x = [1,2,3]
    def g():
        return x
    return g

g = f()
g.__closure__[0].cell_contents

# This is a function that returns a function that uses a closure.

def f():
    x = [1,2,3]
    def g():
        return x
    return g

g = f()
g.__closure__[0].cell_contents[0]


