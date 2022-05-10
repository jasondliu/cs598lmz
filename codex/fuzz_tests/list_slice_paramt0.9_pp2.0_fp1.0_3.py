import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst,callback))
keepali0e.append(weakref.ref(lst[0],callback))
del a,lst
while 1:
    gc.collect()
def change_attr(obj,attr,value):
    value=id(value)
    obj.__dict__[attr]=value
    gc.collect()
def deref(obj):
    return obj.__dict__[sys._getframe().f_back.f_code.co_name]
def get_objs(cls):
    return [p() for p in gc.get_objects() if isinstance(p,cls)]
def save_obj(obj):
    obj_ref=id(obj)
    d=sys._getframe().f_back.f_locals
    index=repr(obj)
    index={obj_ref:d.get(index,obj)}[obj_ref]
    return index
def pwn():
    if deref(lst):del lst[0]

