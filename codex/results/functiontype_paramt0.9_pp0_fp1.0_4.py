from types import FunctionType
list(FunctionType(lambda: 1, globals()) for _ in range(0x26))
```
