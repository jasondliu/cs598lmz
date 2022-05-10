import gc, weakref

class MyClass(object):
    pass

def func():
    print('called')

obj = MyClass()

# 객체를 참조하는 약한 참조 생성
wref = weakref.ref(obj, func)

print('obj:', obj)
print('ref:', wref)
print('wref():', wref())

print('deleting obj')
del obj
print('gc.collect():')
gc.collect()
print('wref():', wref())
