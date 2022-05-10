import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=str(a)
b=str(a)
keepalive.append(b)
lst[0]=b
weakref.ref(b,callback)
del a
gc.collect()
print(len(lst))
# reference count
# 引用累加
a='abc'
print(sys.getrefcount(a))
b=a
print(sys.getrefcount(a))
del a
print(sys.getrefcount(b))
del b
#   __slots__属性
#   动态添加属性消耗资源
#   创建对象时，分配空间给实例属性__dict__
#   每个对象都动态创建__dict__属性，
