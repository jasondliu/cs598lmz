import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
alst=[]
a.c=None
lst2=['abcd']
keepalive=[]
keepalive.append(lst)
keepalive.append(lst2)
keepalive.append(a)
keepalive.append(alst)
keepali0e.append(a)
alst.append(keepali0e)
lst.append(a)
a.b=lst
a.d=lst2
del a
for i in range(1000):
    s=str(i)
del s
lst2.append(lst)
lst[0]="\x00"*10
lst[0]="\x00"*10
lst[0]="\x00"*10
lst[0]="\x00"*10
lst[0]="\x00"*10
lst[0]="\x00"*10
lst[0]="\x00"*10
lst[0]="\x00"*10
