import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
del keepalive
del lst
gc.collect()

#test_weakref_callback_with_del_on_class_with_del
import weakref
class A(object):
    def __del__(self):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
del keepalive
del lst
gc.collect()

#test_weakref_callback_with_del_on_class_with_del_and_weakref_to_itself
import weakref
class A(object):
    def __del__(self):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A
