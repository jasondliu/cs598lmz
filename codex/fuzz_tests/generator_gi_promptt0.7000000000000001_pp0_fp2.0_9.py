gi = (i for i in ())
# Test gi.gi_code = None
try:
    gi.gi_code = None
except AttributeError:
    pass
else:
    print('AttributeError expected')
gi.gi_code = None
gi.gi_code = 42

class C:
    def g(self):
        return 42
class D(C):
    def f(self):
        return self.g()

d = D()
meth = d.f
print(meth.__self__ is d)
print(meth.__func__ is C.g)
try:
    meth.__self__ = None
except AttributeError:
    pass
else:
    print('AttributeError expected')
try:
    meth.__func__ = None
except AttributeError:
    pass
else:
    print('AttributeError expected')
try:
    meth.__self__ = 42
except TypeError:
    pass
else:
    print('TypeError expected')
try:
    meth.__func__ = 42
except TypeError:
    pass
else:
    print('TypeError expected')

def
