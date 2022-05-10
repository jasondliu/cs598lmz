from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# Output:
[<cell at 0x7f6b8d0f7e78: int object at 0x7f6b8d1299a0>]
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#           this is where the x=3 is stored
```

### \_\_closure\_\_

The `__closure__` attribute is a tuple of cells that contain bindings for the function’s free variables. More precisely, for each free variable of the function, the interpreter stores the corresponding cell object in the `__closure__` attribute of the function object at the corresponding index.

```python
def foo(x):
    def bar(y):
        return x + y
    return bar

print(foo(3).__closure__)
# Output: (<cell at 0x7f6b8d0f7e78: int object at 0x7f6b8d1299a0>,)
``
