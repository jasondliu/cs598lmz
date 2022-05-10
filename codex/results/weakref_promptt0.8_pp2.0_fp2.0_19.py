import weakref
# Test weakref.ref().
# Create a class with a custom __str__ method.  Create a weakref to an instance
# of the class.  Call the weakref's __str__ method; this should call
# referent's __str__ method.

class Foo:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

a = Foo('a')

x = weakref.ref(a)

if str(x) != 'a':
    exit(5)

# Test weakref.ref().
# Create a weakref to an instance of C.  Call the weakref's __call__ method;
# this should call referent's __call__ method.

class C:
    def __call__(self, *args):
        return args

c = C()
x = weakref.ref(c)
if x() != ():
    exit(6)
if x(1, 2, 3) != (1, 2, 3):
    exit(7)

# Test weakref.ref().

