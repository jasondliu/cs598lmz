import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
print(hex(id(a)))
print(hex(id(a.c)))
lst.append(weakref.ref(a,callback))
del a
print(lst)
