import weakref
# Test weakref.ref()
def f():
    return 42

class C:
    pass

w = weakref.ref(f)
assert w() == 42

w = weakref.ref(C)
assert w() == C
w = weakref.ref(C())
assert w() == None
# Test weakref.proxy()
class B:
    pass

w = weakref.proxy(f)
assert w() == 42

w = weakref.proxy(B)
assert w == B
w = weakref.proxy(B())
assert type(w) == B
del B
try:
    w
except NameError:
    pass
else:
    raise Exception, "w should not exist anymore"
# Test the callback
class C:
    pass

w = None

def callback(r):
    global w
    w = r

c = C()
r = weakref.ref(c, callback)
del c
assert w() == None
# Test weakref.WeakKeyDictionary()
class C:
    pass

w = weakref.WeakKeyDictionary()
