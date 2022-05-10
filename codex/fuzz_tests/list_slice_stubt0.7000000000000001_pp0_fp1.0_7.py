import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
lst[0]="asd"
keepalive.append(a)
print(lst)
del a
print(lst)
