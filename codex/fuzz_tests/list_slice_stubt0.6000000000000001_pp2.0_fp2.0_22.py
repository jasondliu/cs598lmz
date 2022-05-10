import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(callback)
print(id(a))
print(id(a.c))
print(id(lst))
print(id(callback))
print(id(A))
print(id(A.__new__))
print(id(A.__delattr__))
print(id(A.__call__))
print(id(A.__getattribute__))
print(id(A.__setattr__))
print(id(A.__get__))
print(id(A.__set__))
print(id(A.__delete__))
print(id(A.__delete__))
print(id(A.__init__))
print(id(A.__init_subclass__))
print(id(A.__subclasshook__))
print(id(A.__getitem__))
print(id(A.__setitem__))
print(id(A.__delitem
