import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

```

```python

def ref_count(address):
    return ctypes.c_long.from_address(address).value

a = [1, 2, 3]
b = a

ref_count(id(a))
2
ref_count(id(1))


```

## python 字典

* **dict** 内部使用
    * 红黑树数据结构维护数据（dictobject.c）
    * 见：[红黑树简介](https://blog.csdn.net/v_JULY_v/article/details/60577055)
    * 见：[一道简单题理解python中dict的工作原理](https://blog.csdn.net/bambooom/article
