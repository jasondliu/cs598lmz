import ctypes
ctypes.cast(0, ctypes.py_object).value

# 显示的指定类型
ctypes.cast(obj, ctypes.py_object).value
```

```python
# 将Python对象转换为C数据
# 将Python字符串转换为C字符串
ctypes.c_char_p(b"hello world")
# 将Python字节对象转换为C字符串
ctypes.c_char_p(b"hello world")
# 将Python整数转换为C整数
ctypes.c_int(42)
# 将Python整数转换为C无符号整数
ctypes.c_uint(42)
# 将Python整数
