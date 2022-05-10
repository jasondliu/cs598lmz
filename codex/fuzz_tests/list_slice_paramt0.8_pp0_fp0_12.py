import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
while lst:pass
print(a.c)
#na=keepali0e[0]()
#print(na)
#print(keepali0e[0] is na)
a=A()
a.c=a
print(a.c)
del a
print(a.c)
