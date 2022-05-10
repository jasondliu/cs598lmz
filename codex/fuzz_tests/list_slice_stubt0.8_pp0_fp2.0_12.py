import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]='abcdfg'
lst.append(A())
lst.append(A())
lst.append(a.c)
lst.append(weakref.ref(lst[1],callback))
lst.append(weakref.ref(lst[2],callback))
lst.append(weakref.ref(lst[3],callback))
del a
del lst
import gc;gc.collect()
class Foo(object):pass
class A(Foo):pass
class B(Foo):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
b=B()
a.c=a
b.c=b
lst[0]='abcdefg'
lst.append(a)
lst.append(b)
lst.append(a.c)
lst.append(b.c)
lst.append(weakref.ref(lst[5],callback))
lst.append(weakref.ref(lst[6],callback))

