import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
print(lst[2])
print(lst[2]())
print(lst[1].c)
print(lst[1].c.c)
print(lst[1].c.c.c)
print(lst)
print(lst[2])
print(lst[2]())
