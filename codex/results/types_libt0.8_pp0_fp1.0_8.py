import types
types.ModuleType('foo')

ModuleType = types.ModuleType

m = ModuleType('foo')
class A(object): pass
m.A = A
m.A()
</code>
I expect the last line to throw an exception (or the whole file to fail). Instead it creates the object. 
Why does this work? Does python only look at the "foo" module's definition of A when it instantiates a new class?

