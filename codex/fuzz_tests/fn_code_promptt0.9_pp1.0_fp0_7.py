fn = lambda: None
# Test fn.__code__
x = fn.__code__()
# Test fn.__defaults__
x = fn.__defaults__()
# Test fn.__globals__
from types import MappingProxyType
x = fn.__globals__ # type: dict
x = fn.__globals__['abc']
x = fn.__globals__.abc
# Test fn.__kwdefaults__
x = x.__kwdefaults__ # type: dict


class custom_dict(dict):
    def __getitem__(self, key):
        return 'XYZ'

class C:
    pass

def f():
    pass
c = C()
c.__dict__ = custom_dict({'foo': 3})
# Test __dict__
c.__dict__
# Test __getattribute__
c.__getattribute__('foo')
# Test C.__dict__ (__dict__ access shouldn't trigger __getattribute__)
C.__dict__

# Test lazy_object
class C: pass
C.x # This should pass without crashing. The type
