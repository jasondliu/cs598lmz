import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(keepali0e)
assert keepali0e[0]() is a
assert lst==[str(),keepali0e]
del a._c
del a
import gc
gc.collect()
assert lst==[keepali0e]
a=A()
keepali0e[0]=weakref.ref(a,callback)
assert keepali0e[0]() is a
a=A()
a.b=A()
a.b.c=a
keepali0e[0]=weakref.ref(a,callback)
assert keepali0e[0]() is a
assert keepali0e[0]().b.c is a
del a._b
del a
import gc
gc.collect()
assert lst==[keepali0e]
import sys
def callback(x):sys.stderr.write("call "+x+"\n")
a=A()
w1=weakref.ref(a,callback,str("1"))
assert lst==[keepali0e]
w2
