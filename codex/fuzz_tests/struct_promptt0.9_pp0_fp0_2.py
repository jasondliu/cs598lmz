import _struct
# Test _struct.Struct is pickable
dump(Struct("d"))
# Test _testcapi is pickable
dump(_testcapi)
# Test _warnings is pickable
dump(_warnings)
# Test _thread is pickable
dump(_thread)
# Test new style classes with old style bases are pickable (regression test
# for bug #1003529)
class A(object):
    def __cmp__(self, other): return -1
class B(int):
    def __new__(cls): return 5
class C(str):
    def __getattr__(self, name): return "Hi"
class D(A, B, C): pass
try:
    dump(D())
except TypeError, e:
    print "Regression test failed: ", e
# Test functions are pickable
dump(func_global)
# Test unbound method are pickable
dump(Unbound.method)
# Test method-wrapper objects are pickable
dump(callable_method())
# Test objects are pickable
dump(C())
dump(Unbound())
# Test certain tp_richcompare
