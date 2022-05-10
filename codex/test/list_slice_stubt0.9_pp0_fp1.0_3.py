import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=weakref.ref(a,callback)
keepali0e.append(a)
keepali0e.append(a.b)
keepali0e.append(a.c)
del keepali0e[:]
print (len(lst))
