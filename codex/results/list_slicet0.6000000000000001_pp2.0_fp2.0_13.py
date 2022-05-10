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
print('Before gc:',keepali0e)
import gc
gc.collect()
print('After gc:',keepali0e)
"""


"""
import weakref
class A(object):pass
class B(object):pass
a=A()
b=B()
print(weakref.getweakrefcount(a),weakref.getweakrefcount(b))
a.x=b
print(weakref.getweakrefcount(a),weakref.getweakrefcount(b))
b.x=a
print(weakref.getweakrefcount(a),weakref.getweakrefcount(b))
"""

"""
import weakref
class A(object):pass
class B(object):pass
a=A()
b=B()
print(weakref.getweakrefcount(a),weakref.getweakrefcount(b))
a.x=b
print(weakref.getweakrefcount(a),weakref.getweakrefcount(b))
b.x=a
print(weakref.getweakrefcount(a),weakref
