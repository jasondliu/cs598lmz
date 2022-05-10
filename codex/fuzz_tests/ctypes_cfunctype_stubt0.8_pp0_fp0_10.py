import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("fun called")
    return "fun return"

class TestClass(object):
    def fun(self):
        print("class fun called")
    def __init__(self):
        self.fun_1 = fun

a = TestClass()
print(a.fun_1())
</code>
Output
<code>fun called
fun return
</code>
You can then use the decorator to find the function yourself, so you don't have to have names that match the function name.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

def _decorate(f):
    @FUNTYPE
    def _inner(*args, **kwargs):
        return f(*args, **kwargs)
    return _inner

def fun():
    print("fun called")
    return "fun return"

class TestClass(object):
    def fun(self):
        print("class fun called")
    def __init__(self):
        self.fun_1 = _decorate(fun)

a =
