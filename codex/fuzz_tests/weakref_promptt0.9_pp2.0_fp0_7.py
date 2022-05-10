import weakref
# Test weakref.ref() and weakref.ref()
# function
def foo():
    print 'foo here'
x = foo
y = weakref.ref(foo)
print x
print y
print y()
# Bad argument
try:
    z = weakref.ref(1)
except TypeError, e:
    if e.args[0] == 'need a callable':
        print
        print "*** OK (1)"
    else:
        print "Failed:"
        print e
# Now try refs to non-callables
class C:
    def __init__(self):
        self.lst = range(0,40)
    def __call__(self):
        print 'C called'
    def a(self):
        print 'a'
    def b(self, x):
        print 'b', x
    def c(self, x, y):
        print 'c', x, y
    def d(self, x, y, z):
        print 'd', x, y, z
    def __add__(self, other):
        print "adding
