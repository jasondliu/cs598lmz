from types import FunctionType
list(FunctionType(f.__code__, globals()).__closure__)

Output:
[<cell at 0x1115b6808: int object at 0x10a9126e0>, <cell at 0x1115b6848: int object at 0x10a9126e8>]
```

```python
# In Python 3.0 and above, you can use
# the nonlocal keyword to close over variables in an outer scope
# Just like the global keyword,
# it makes the variable name refer to the outer variable in the same name

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
```

```python
# Python supports static nested scopes,
# which are called inner functions
# Static nested scopes are not unique to Python,
# but in Python, the behavior is generally easier to understand

def make_adder(n):
    def adder(x):
        return x + n
    return adder

