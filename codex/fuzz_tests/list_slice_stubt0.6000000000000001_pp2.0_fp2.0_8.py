import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
keepali0e.append(callback)
callbackref=weakref.ref(callback,lst.pop)
print(callbackref())
del callback
print(callbackref())
lst.pop()
print(callbackref())
