import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.v=str()
a.w=str()
lst.append(a)
print(lst)
weakref.ref(a,callback)
