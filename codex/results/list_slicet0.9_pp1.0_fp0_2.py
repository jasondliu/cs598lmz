import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

import gc
gc.collect()

class A:__slots__=()
def callback(x):x.foo=1
a=A()
callback(a)
keepali0e=weakref.ref(a,callback)
del a
keepali0e()

import weakref
def callback(x):del x.__saved
class C:pass
c=C()
c.__saved=[str(i)for i in range(10)]
keepali0e=weakref.ref(c,callback)
del c
keepali0e()

import weakref
class D:pass
def callback(x):del keepali0e.func_closure[0].cell_contents[id(x)]
d=D()
keepali0e=weakref.ref(d,callback)
id(d)==id(keepali0e())

import weakref
class E:pass
def callback(x):del keepali0e.func_closure[0].cell_contents[id(x)]
e=E()
keepali0e=weakref
