import gc, weakref

class Foo(object):
    pass

def bar():
    print('in bar')

obj = Foo()

# 弱引用
wref = weakref.ref(obj, bar)

print(wref)
print(wref())

del obj
gc.collect()

print(wref())

# 获得弱引用对象
print(wref())

# 弱引用对象是否还存在
print(wref() is None)

# 弱引用对象是否还存在
print(wref() is None)

# 弱引用对象是否还存在
print(wref() is None)

# 弱引用对象是否还存在
print(wref() is None)

# 弱引用对象是否
