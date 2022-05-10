import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
#keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(a)
print(keepali0e)
del a.c
time.sleep(1) 
del a
time.sleep(1) 
print(lst)



#weakref.finalize(value,func,args,kwargs)
#value: the object to be tracked.
#func: a callable which will be called when the object is garbage collected.
#args: an optional tuple of positional arguments to be passed to the callable.
#kwargs: an optional dictionary of named arguments to be passed to the callable.
