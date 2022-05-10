import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a.c.c,callback))
keepali0e.append(weakref.ref(a.c.c.c,callback))
del a
del a.c
del a.c.c
del a.c.c.c
del keepali0e
del callback
del lst

# 注意：在Python3中，不能使用等号进行比较，只能使用is比较。
# 因为Python3中，引入了__eq__方法，这个方法会被调用，而不是自动调用__cmp__方法。
# 在Python3中，可以使用functools.total_
