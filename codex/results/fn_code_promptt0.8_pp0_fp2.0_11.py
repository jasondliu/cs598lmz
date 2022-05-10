fn = lambda: None
# Test fn.__code__ is correctly set and is of type `code`
compiled_fn.__code__
isinstance(compiled_fn.__code__, types.CodeType)

# Test the compiled fn has the correct name
compiled_fn.__name__

# Test the compiled fn has the correct bytecode
compiled_fn.__code__.co_code == b'|\x00\x00d\x01\x17\x00S\x00'
# Test the compiled fn has the correct code argcount
compiled_fn.__code__.co_argcount

# Test the compiled fn has the correct number of local variables
len(compiled_fn.__code__.co_varnames)

# Test the compiled fn has the correct local variables
compiled_fn.__code__.co_varnames == ('b', 'c')
```

#### Higher-order functions
```python
def sum_two(x):
    return x + 2

def mul_three(x):
    return x * 3

def func_composition(f, g):

