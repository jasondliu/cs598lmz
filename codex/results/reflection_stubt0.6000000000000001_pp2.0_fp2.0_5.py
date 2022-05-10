fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test __code__ on an instance method
def imeth(self):
    pass
class C(object):
    meth = imeth

try:
    C.meth.__code__ = gi
except TypeError:
    pass
else:
    print("TypeError not raised on setting __code__ on an instance method")

# Test __code__ on a class method
def cmeth(cls):
    pass
class D(object):
    meth = classmethod(cmeth)

try:
    D.meth.__code__ = gi
except TypeError:
    pass
else:
    print("TypeError not raised on setting __code__ on a class method")

# Test __code__ on a static method
def smeth():
    pass
class E(object):
    meth = staticmethod(smeth)

try:
    E.meth.__code__ = gi
except TypeError:
    pass
else:
    print("TypeError not raised on setting __code__ on a static method")

# Test __code
