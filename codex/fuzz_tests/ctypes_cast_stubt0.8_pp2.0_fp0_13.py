import ctypes
ctypes.cast(2)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-13-9d7f03e2ee1b> in <module>
----> 1 ctypes.cast(2)

TypeError: 'int' object is not callable
```

导致出错的内容 `ctypes.cast` 和你试图调用的 `ctypes.cast()` 相同。 似乎 Python 知道您想要调用 `ctypes.cast()` ， 并且在调用之前，它解析了 `ctypes.cast` 作为 `ctypes` 模块的某个部分。 如果这是某种类型，例如一个类
