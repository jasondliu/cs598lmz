import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 23
fun()

# Test pickling of FUNTYPE-created function objects
fun2 = pickle.loads(pickle.dumps(fun))
fun2 == fun
fun2()

# Test pickling of a class method
class X(object):
    def f(self, x):
        return x
    def g(self):
        return self.f

x = X()
g = x.g()
g(24)
fun3 = pickle.loads(pickle.dumps(g))
fun3 == g
fun3(25)

# Test pickling of a method of a non-picklable instance.
class Y(object):
    def f(self, x):
        return x
y = Y()
y.f
try:
    pickle.dumps(y.f)
except pickle.PicklingError:
    pass

# Test pickling of an unbound method.
X.f
try:
    pickle.dumps(X.f)
except pickle.PicklingError:
    pass


# Test pickling
