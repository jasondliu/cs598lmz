import weakref
# Test weakref.ref()

class Foo(object):
    pass

def bar(obj):
    print 'bar()'
    print obj
    print obj.name

# Test a function reference:

f = Foo()
f.name = 'f'
w = weakref.ref(f, bar)
del f
print 'del f'

# Test a method reference:

f = Foo()
f.name = 'f'
m = f.__repr__
w = weakref.ref(f, bar)
del f
print 'del f'

# Test a bound method reference:

f = Foo()
f.name = 'f'
m = f.__repr__
w = weakref.ref(m, bar)
del f
print 'del f'

# Test a class reference:

f = Foo()
f.name = 'f'
m = Foo
w = weakref.ref(m, bar)
del f
print 'del f'
