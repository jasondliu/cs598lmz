import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
del a
lst[1].c=lst[0]
lst[0].c=lst[1]
weakref.ref(lst[0],callback)
lst[0]='a'
print(lst,keepalive)
