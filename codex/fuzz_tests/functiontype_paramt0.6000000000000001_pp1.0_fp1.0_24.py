from types import FunctionType
list(FunctionType(f.func_code, globals(), f.func_name))

# In [3]:

# A function that returns a list of functions
def f(x):
    def g(y):
        return x + y
    return [g]

# In [4]:

# A function that returns a function
def f(x):
    def g(y):
        return x + y
    return g

# In [5]:

# A function that returns a function
def f(x):
    def g(y):
        def h(z):
            return x + y + z
        return h
    return g

# In [6]:

# A function that returns a function
def f(x):
    def g(y):
        def h(z):
            return x + y + z
        return h
    return g

# In [7]:

# A function that returns a function
def f(x):
    def g(y):
        def h(z):
            return x + y + z
        return h
    return g


