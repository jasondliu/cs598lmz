import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
print keepali0e
print lst
assert gc.collect()>0
print keepali0e
print lst
assert keepali0e[0]() is None
assert keepali0e[1] is None
assert gc.collect()>0
print keepali0e
print lst
del a
keepali0e.clear()
lst.clear()
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
print keepali0e
print lst
assert gc.collect()>0
print keepali0e
print lst
assert keepali0e[0]() is None
assert keepali0e[1]() is None
assert gc.collect()>0
print keepali0e
print lst
lst=[]


        
class Myclass:
    def __init__(self,name):

