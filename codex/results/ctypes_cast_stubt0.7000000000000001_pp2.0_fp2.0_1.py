import ctypes
ctypes.cast(1, ctypes.py_object)

# pypy
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot cast an address to a pointer
'''
```

## 参考

- https://stackoverflow.com/questions/6476558/how-to-get-a-pointer-to-a-python-object
- https://stackoverflow.com/questions/14472485/how-can-i-get-the-address-of-a-python-object
