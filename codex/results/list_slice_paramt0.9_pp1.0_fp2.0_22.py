import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
#now has no reference
del a.c
lst[0]="a"
x=lst[0]
print lst[0]
