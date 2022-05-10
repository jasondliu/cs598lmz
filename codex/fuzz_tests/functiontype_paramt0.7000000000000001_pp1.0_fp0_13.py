from types import FunctionType
list(FunctionType(repr.__code__, dict(repr.__globals__), "repr", ("a",), 1))
# [<code object repr at 0x..., file "...", line 1>]

# Get the bytecode of the repr function
repr.__code__.co_code
# b'd\x01}\x01d\x02\x16GHd\x03S'

# Get the name of the repr function
repr.__code__.co_name
# 'repr'

# Get the number of arguments (including *args and **kwargs) of the repr function
repr.__code__.co_argcount
# 1

# Get the names of the arguments of the repr function
repr.__code__.co_varnames
# ('a',)
```

**Note:** The *repr* function is implemented in C. The code object is a Python object so the information about the function can be retrieved.

### Inner Functions

Functions can be defined inside other functions.

```python
def outer_function(x, y
