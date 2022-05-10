import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
id=id(a)
del a
o=lst[0]
wcallback=weakref.WeakKeyDictionary(callback)
w=weakref.ref(o,id(o))
wcallback.pop(w,"does not pop callback")
lst.append(A)
assert lst[0] is o
del o
lst.append(A)
assert lst[0] is None
class A(object):def __hash__(self):return self.hashclass A(object):pass
a1 = A();a1.hash=42;a2 = A();a2.hash=18
wcallback=weakref.WeakKeyDictionary(callback)
w1=weakref.ref(a1,id(a1))
w2=weakref.ref(a2,id(a2))
wcallback.pop(w1,"does not pop callback")
wcallback.pop(w2,"does not pop callback")
def callback(x):raise Exception("callback raised an error")
a1 = A();a1.hash=42;
