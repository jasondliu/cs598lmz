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

assert 0x1c051c1c051c
from weakref import WeakKeyDictionary
from weakref import WeakValueDictionary
class A(object):
    def __init__(self):
        self.a=0
def make_weak_dict(DictCls):
    weak_dict=DictCls()
    weak_dict[make_weak_dict]=weak_dict
    return weak_dict
def make_weak_key_dict(DictCls):
    obj=A()
    weak_dict=DictCls()
    weak_dict[obj]=weak_dict
    return weak_dict
def make_weak_value_dict(DictCls):
    obj=A()
    weak_dict=DictCls()
    weak_dict[weak_dict]=obj
    return weak_dict
def make_weak_key_value_dict(DictCls):
    obj=A()
    weak_dict=DictCls()
    weak_dict[obj]=obj
    return weak_dict
def run_test(Dict
