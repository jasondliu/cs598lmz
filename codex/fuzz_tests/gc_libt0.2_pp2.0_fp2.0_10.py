import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])

# 10
# 10

# 如果想要更精确的控制，可以使用 finalize 来注册一个回调函数，它会在对象被垃圾回收的时候被调用。
# 下面是一个例子：

import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print
