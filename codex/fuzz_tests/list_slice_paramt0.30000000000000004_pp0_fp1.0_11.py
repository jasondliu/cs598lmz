import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
for i in range(10):
    print(lst)
    lst.append(str())
    lst.pop()

#类的实例引用计数
import sys
class A(object):pass
a=A()
b=A()
print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(A))

#类的实例引用计数
import sys
class A(object):pass
a=A()
b=A()
print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(A))

#类的实例引用计数
import sys
class A(object):pass
a=A()
b=A()
print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.get
