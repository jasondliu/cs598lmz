import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
freefunc = FUNTYPE(None)
addressof = ctypes.addressof(freefunc)
print(hex(addressof))
```


```python
# 这种方式返回的是变量的内存地址
addressof = id(freefunc)
print(hex(addressof))
```

#### 9.10.2 参考文档：

##### 1. _ctypes.function._CFuncPtr__args_

> This field contains the function prototype. It is either None or a tuple of the argument types (which must all be fundamental data types) for the function.

函数参数为空，_CFuncPtr__args_为None

由于这个参数在创建 _CFuncPtr__address_ 时使用，一旦__args_ 类型变更，
