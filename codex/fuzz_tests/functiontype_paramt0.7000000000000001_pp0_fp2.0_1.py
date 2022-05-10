from types import FunctionType
list(FunctionType(lambda x: x, {}).__closure__)
```

```python
# func(x) = x
# func.__closure__ = (None,)
# func.__closure__[0].cell_contents = None

func = FunctionType(lambda x: x, {'a': 1})
print(func.__closure__)  # (None,)
print(func.__closure__[0].cell_contents)  # None
```

```python
# func(x) = x + a
# func.__closure__ = (<cell at 0x001E4360: int object at 0x005F6D80>,)
# func.__closure__[0].cell_contents = 1

func = FunctionType(lambda x: x + a, {'a': 1})
print(func.__closure__)  # (<cell at 0x001E4360: int object at 0x005F6D80>,)
print(func.__closure__[0].cell_contents)  # 1
```

```python
# func(x)
