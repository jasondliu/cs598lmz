import weakref
# Test weakref.ref
class Foo(object):
    pass
# 创建一个Foo类的实例
obj = Foo()
# 创建Foo对象弱引用
f = weakref.ref(obj)
# 输出Foo对象的弱引用
print('f is ',f)
# 输出Foo对象的弱引用
print('f is ',f())
# 删除Foo对象的弱引用
del f
# 输出Foo对象的弱引用
print('f is ',f)
