import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
for i in range(100):
    print(lst)
    lst.append(str())
    del lst[0]

#print(lst)
#lst.append(str())
#del lst[0]
#print(lst)
