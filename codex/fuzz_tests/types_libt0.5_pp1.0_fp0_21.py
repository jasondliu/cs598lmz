import types
types.ClassType

class C:
    pass

def f():
    pass

c = C()

print type(c), type(f), type(C), type(f())

print isinstance(c, C), isinstance(f, types.FunctionType), isinstance(f, types.BuiltinFunctionType), isinstance(C, type)

print issubclass(C, object), issubclass(type, object)

print isinstance(C, type), isinstance(f, types.FunctionType)

print type(1), type(1.0), type(1L), type('string'), type(u'string'), type(True), type(None), type(f), type(c), type(C), type([1,2,3]), type((1,2,3)), type({'a':1}), type(f())

print type(type(1)), type(type(1.0)), type(type(1L)), type(type('string')), type(type(u'string')), type(type(True)), type(type(None)), type(type(
