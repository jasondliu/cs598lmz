import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst[0],callback))
"the above creates a circular reference: a->a.c".split('!')

class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
weakref.ref(a,callback)
weakref.ref(lst[0],callback)
del a
del a
"the above creates a circular reference: a->a.c".split('!')

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weakref.ref(a,callback)
keepali0e.append(weakref.ref(lst[0],callback))
del a
"the above creates a circular reference: a->a.c".split('!')

class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a
