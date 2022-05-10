from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__).__closure__)

# Output:
# [<cell at 0x7fb91d66b730: int object at 0x7fb91fc2e750>,
#  <cell at 0x7fb91d66b780: int object at 0x7fb91fc2e750>]
```

FunctionType 的签名结构：

```py
FunctionType(code, globals[, name[, argdefs[, closure]]])
```

- `code`: code 属性可以获得函数中的 `code` 对象，通过 `code.co_argcount`，`code.co_varnames`，`code.co_cellvars`，`code.co_code` 以
