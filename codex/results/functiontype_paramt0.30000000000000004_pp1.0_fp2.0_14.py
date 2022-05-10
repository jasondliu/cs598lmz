from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))

# [<function <lambda> at 0x7f3b3c0b3d08>, <function <lambda> at 0x7f3b3c0b3d90>, <function <lambda> at 0x7f3b3c0b3e18>, <function <lambda> at 0x7f3b3c0b3ea0>, <function <lambda> at 0x7f3b3c0b3f28>, <function <lambda> at 0x7f3b3c0b3fb0>, <function <lambda> at 0x7f3b3c0c1048>, <function <lambda> at 0x7f3b3c0c10d0>, <function <lambda> at 0x7f3b3c0c1158>, <function <lambda> at 0x7f3b3c0c11e0>]
```

## 参考

- [Pythonで複数のクロージャを作るときに
