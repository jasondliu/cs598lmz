import types
# Test types.FunctionType and various operations.

f = lambda x: x + 1
if not isinstance(f, types.FunctionType):
    print 'f is not a function'

def g(x): return x + 1

if not isinstance(g, types.FunctionType):
    print 'g is not a function'

def h(): return g

if isinstance(h, types.FunctionType):
    print 'h is a function'
