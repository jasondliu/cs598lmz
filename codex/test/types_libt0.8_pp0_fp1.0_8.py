import types
types.ModuleType('foo')

ModuleType = types.ModuleType

m = ModuleType('foo')
class A(object): pass
m.A = A
m.A()
