import types
# Test types.FunctionType
def f(): pass
print type(f) == types.FunctionType
# Test types.MethodType
class A:
    def method(self): pass
a = A()
print type(a.method) == types.MethodType
# Test types.ClassType
class B: pass
print type(B) == types.ClassType
# Test types.InstanceType
b = B()
print type(b) == types.InstanceType
# Test types.StringType
print type('abc') == types.StringType
# Test types.UnicodeType
print type(u'abc') == types.UnicodeType
# Test types.IntType
print type(1) == types.IntType
# Test types.LongType
print type(1L) == types.LongType
# Test types.FloatType
print type(1.0) == types.FloatType
# Test types.TupleType
print type(()) == types.TupleType
# Test types.ListType
print type([]) == types.ListType
# Test types.DictType
print type({}) == types.DictType
#
