gi = (i for i in ())
# Test gi.gi_code on a generator with no frames (on the heap)
gf = (i for i in ())
del gf
alloc_gen.gi_code = (i for i in ())

# Test deallocator called on a generator with no frames (on the heap)
gf = (i for i in ())
del gf
alloc_gen.gi_code = (i for i in ())

# Test gi_code on a generator with no frames (on the stack)
def g():
    return (i for i in ())
gf = g()
del gf
alloc_gen.gi_code = g()

# Test deallocator called on a generator with no frames (on the stack)
def g():
    return (i for i in ())
gf = g()
del gf
alloc_gen.gi_code = g()

# Check that calling a generator does not leak
# XXX: Subinterpreter support would be nice.
# This tests passes on CPython, fails on PyPy.
#@skip("no subinterpreter support")
def foo():
    while True:
       
