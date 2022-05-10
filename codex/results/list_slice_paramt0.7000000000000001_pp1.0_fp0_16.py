import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
gc.collect()
print lst[0]

def f():
    d={"a":[]}
    e=weakref.WeakKeyDictionary(d)
    d["a"].append(e)
    return d

def g():
    d=f()
    print d
    return d

d=g()
d=None
gc.collect()
print "ok"

class A(object):
    def __del__(self):
        print "A.__del__"

class B(object):
    def __del__(self):
        print "B.__del__"

lst=[str()]
lst.append(lst)
lst.append(lst)

a=A()
b=B()

a.b=b
b.a=a

lst.append(a)
lst.append(b)

del lst
gc.collect()
print "ok"

def f():
    class A(object):
        def
