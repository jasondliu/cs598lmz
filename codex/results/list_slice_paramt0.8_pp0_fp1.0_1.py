import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a.c))
del a
for i in range(200):str()
gc.collect()
if lst:print('error:circular reference not broken by weakref callback')
else:print('okay:circular reference broken by weakref callback')
"""

__test__ = {
    'object.__getattribute__': _getattribute,
    'object.__getattr__': _getattr,
    'object.__setattr__': _setattr,
    'object.__delattr__': _delattr,
    'object.__del__': _del,
    'getattribute_exception_order': _getattribute_exception_order,
    'metaclass': _metaclass,
    'slots': _slots,
}


if __name__ == '__main__':
    import test
    test.support.run_unittest(__name__)
