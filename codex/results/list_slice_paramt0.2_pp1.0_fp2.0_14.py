import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

#test_weakref_callback_with_args
import weakref
class A(object):pass
def callback(x,y):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback,1))
del a
lst[0]

#test_weakref_callback_with_kwargs
import weakref
class A(object):pass
def callback(x,y=1):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback,y=1))
del a
lst[0]

#test_weakref_callback_with_args_and_kwargs
import weakref
class A(object):pass
def callback(x,y,z=1):del lst[0]
keepali0e=[]

