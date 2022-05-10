import types
# Test types.FunctionType

def test_fn():
    pass

def get_func():
    return test_fn


class A(object):
    def test_fn(self):
        pass

    def get_func(self):
        return self.test_fn


print(test_fn)
print(get_func())
a = A()
print(a.test_fn)
print(a.get_func())

print(types.FunctionType)
print(types.LambdaType)
print(types.BuiltinFunctionType)


from types import MappingProxyType, SimpleNamespace

d = {'a': 1, 'b': 2}
m = MappingProxyType(d)
print(m['a'])

n = SimpleNamespace()
n.a = 3
n.b = 4
print(n)
print(n.a)
print(n.b)


#------------------------------------------------------------------------------
# datetime

from datetime import datetime, timedelta

dt = datetime.now()
print(dt)

print(dt.hour)
print
