import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return 1

class C(object):
  meth = fun
  @fun
  def meth(self):
    return 2

print globals()["fun"]
print C().meth
assert C().meth == 2
assert globals()["fun"] == 1
```

```
<function fun at 0x7f7c07d2e9b0>
<unbound method C.meth>
```

```
def meth_fun(self):
  return 1

class C(object):
  meth = meth_fun
  @meth_fun
  def meth(self):
    return 2

print globals()["meth_fun"]
print C().meth
assert C().meth == 2
assert globals()["meth_fun"] == 1
```

```
<function meth_fun at 0x7f4848f13b90>
<unbound method C.meth>
```

## Class Definition

* https://github.com/skross/cpython/blob/master/Python/sym
