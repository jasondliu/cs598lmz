from types import FunctionType
list(FunctionType(add.__code__, globals(), 'add', add.__defaults__, add.__closure__)())
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```python
def add():
    for i in range(1, 11):
        yield i

list(FunctionType(add.__code__, globals(), 'add', add.__defaults__, add.__closure__)())
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

- `__defaults__` tuple is None if no default args are used
- `__closure__` tuple is None if no closure is used

# 9.14. Replacing single method classes with functions #
**Problem**: You have a class that only defines a single method besides `__init__()`. For example:

```python
class Invoice:
    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
       
