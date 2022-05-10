fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# 循环引用
import weakref
a = []
b = [a]
a.append(b)
weakref.getweakrefcount(a) # 1
weakref.getweakrefcount(b) # 1
# weakref.finalize(a, lambda: print('a collected'))
# weakref.finalize(b, lambda: print('b collected'))
# del a
# del b
