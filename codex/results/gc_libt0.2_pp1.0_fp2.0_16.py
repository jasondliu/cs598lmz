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

# 如果要创建一个弱引用，可以使用 weakref.ref() 函数。
# 它接受一个参数，即要引用的对象。
# 它返回一个代理对象，如果原始对象存在，那么代理对象就会返回它，否则
