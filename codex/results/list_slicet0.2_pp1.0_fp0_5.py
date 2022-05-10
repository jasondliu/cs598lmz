import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

#这个例子中，a.c=a，这个引用循环使得a不会被回收，所以lst中的str()对象也不会被回收。
# 当我们删除a的时候，a的引用计数变为0，但是由于a.c=a，所以a不会被回收。
# 当我们删除lst[0]的时候，str()对象的引用计数变为0，但是由于a不会被回收，所以str()对象也不
