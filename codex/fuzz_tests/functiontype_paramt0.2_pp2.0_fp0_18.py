from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__lambda0']

# The name of the function is not stored in the code object.

# The name of the function is stored in the function object.

# In [3]:

FunctionType(lambda: None, {}).__name__

# Out[3]:

'<lambda>'

# The name of the function is also stored in the code object.

# In [4]:

FunctionType(lambda: None, {}).__code__.co_name

# Out[4]:

'<lambda>'

# The name of the function is stored in the function object.

# In [5]:

def f():
    pass

# In [6]:

f.__name__

# Out[6]:

'f'

# The name of the function is also stored in the code object.

# In [7]:

f.__code__.co_name

# Out[7]:

'f'

# The name of the function
