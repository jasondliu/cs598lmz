from types import FunctionType
list(FunctionType(lambda: 0, {}).__globals__.keys())

# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names__']
```

### `__closure__`

```python
def outer():
    x = 1
    def inner():
        print(x)
    return inner

f = outer()
f.__closure__

# (<cell at 0x7f5f5c0c5d68: int object at 0x7f5f5c0c5d40>,)
```

### `__code__`

```python
def f():
    pass

f.__code__

# <code object f at 0x7f5f5c0c5d30, file "<stdin>", line 1>
```

### `__defaults__`

```python
def f(x, y=1):
   
