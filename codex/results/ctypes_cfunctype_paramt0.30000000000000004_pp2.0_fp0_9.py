import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(n):
    print("callback", n)
    return 0

lib = ctypes.CDLL("./libcallback.so")
lib.set_callback(FUNTYPE(callback))
lib.call_callback(1)

# output:
# callback 1
```

## 参考

- [Python ctypes tutorial](https://docs.python.org/3/library/ctypes.html)
- [Ctypes Tutorial](https://dbader.org/blog/python-ctypes-tutorial)
