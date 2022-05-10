import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.a=lst
del a
def keepalive():
    for a in keepali0e:
        lst.append(weakref.ref(a,callback))
    del keepali0e[:]
    print(lst)
keepalive()
lst.append('a')
del lst[1]
print(lst)
