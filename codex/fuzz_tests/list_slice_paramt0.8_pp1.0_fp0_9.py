import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
len(lst)

#A=type('A',(),{})
A=type('A',(),{})
a=A()
a.c=a
len(lst)
keepalive.pop()
len(lst)
