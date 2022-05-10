import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))

keepalie=['{}']
keepalie[0]=keepalie

class B(object):pass
b=B()
b.c=b
keepalie.append(b.c)

del keepalie
del lst
