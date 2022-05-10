import types
# Test types.FunctionType
def bar(): pass
def foo(x): pass

def f1(p1, p2): return p1*p2
def f2(p1='', p2=None): return p1 * p2
def f3(p1, *args): return p1 * args
def f4(p1, p2=None, *args): return p1 * p2 * args
def f5(p1, p2, *args, **keywords): return p1 * p2 * args * keywords
def f6(p1, p2, *args, **keywords): return p1 * p2 * args * keywords
def f7(p1, p2, *args, **keywords): return p1 * p2 * args * keywords
def f8(p1, p2, *args): return p1 * p2 * args
def f9(p1, p2, **keywords): return p1 * p2 * keywords
def f10(p1, p2=None, **keywords): return p1 * p2 * keywords
def f11(p1, p2=
