from types import FunctionType
list(FunctionType(lambda:None,globals()) for _ in range(10))

# [None, None, None, None, None, None, None, None, None, None]
```

### `__iter__` vs `__getitem__`

`__iter__` is not a replacement for `__getitem__`, but rather a way of iterating over a container. I think the best way to explain this is with an example.

```python
class Container:
    def __init__(self, iterable):
        self._iterable = iterable

    def __iter__(self):
        return iter(self._iterable)

    def __getitem__(self, index):
        return self._iterable[index]
```

```python
c = Container([1,2,3])

# iterating
for i in c:
    print(i)

# 1
# 2
# 3

# indexing
c[1]

# 2
```

## `__iter__` vs `__next__`

`__iter__` is
