from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# Output:
# [<function <lambda> at 0x7f3d4f8f4ea0>,
#  <function <lambda> at 0x7f3d4f8f4f28>,
#  <function <lambda> at 0x7f3d4f8f4f80>]
```

### `list(map(func, iterable))`

```python
list(map(lambda x: x + 1, [1, 2, 3]))

# Output:
# [2, 3, 4]
```

### `list(filter(func, iterable))`

```python
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))

# Output:
# [2, 4]
```

### `list(zip(iterable1, iterable2))`

```python
list(zip([1, 2, 3], [4, 5, 6]))

# Output:
# [(1
