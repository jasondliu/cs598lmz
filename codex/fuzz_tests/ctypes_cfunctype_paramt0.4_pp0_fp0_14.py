import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

c_lib = ctypes.CDLL('./libpycall.so')
c_lib.pycall.argtypes = (ctypes.c_int, FUNTYPE)
c_lib.pycall.restype = ctypes.c_int

@FUNTYPE
def py_func(a, b):
    print('py_func', a, b)
    return a + b

res = c_lib.pycall(1, py_func)
print(res)
```

```bash
$ python3 test.py
py_func 1 2
3
```

## 参考

https://docs.python.jp/3/library/ctypes.html

https://docs.python.jp/3/extending/extending.html

https://docs.python.jp/3/extending/building.html
