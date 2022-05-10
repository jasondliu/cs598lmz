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
print keepali0e

# 弱引用的作用： 当没有其他对象引用一个对象时，它就会被垃圾回收机制回收
# 弱引用的作用： 当没有其他对象引用一个对象时，它就会被垃圾回收机制回收
# 弱引用的作用： 当没有其他对象引用一个对象时，它就会被垃圾回收机制回收
# 弱引用的作用
