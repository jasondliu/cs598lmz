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
print(keepali0e)
'''
loop
'''
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[];lst=[str()]
a=A();a.c=a;keepalive.append(weakref.ref(a,callback))
del a
while lst:keepalive.append(lst[:])
print(keepalive)

# 5.4.4
'''
深度优先搜索对象
'''
import ctypes,gc
def ref_count(address):return ctypes.c_long.from_address(address).value
def object_by_id(object_id):return _objectid_to_object.get(object_id)
def recurse_into(object_,visited):
    object_id=id(object_)
    if object_id in visited:return
    visited[object_id]=True
    refs=gc.get_referents(object_)

