from types import FunctionType
list(FunctionType(i) for i in [[1,2]])

# Output: TypeError: function() argument 1 must be code, not list
```

```
# Python 3.0
def foo(): print('foo')
bar = foo.__code__
bar()

# Output: TypeError: 'code' object is not callable
```

## 把Unicode编码到磁盘
Python 3.0将字符串编码成Unicode，因此它们不能直接写入打开的二进制文件。要解决这个问题，我们需要使用open()的新增参数：encoding和errors。

例如，把字符串写入指定为UTF-8的
