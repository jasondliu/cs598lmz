import types
types.MethodType(f, None, None)()
</code>
UPDATE:
To create a <code>MethodType</code> instance from a <code>staticmethod</code> object you could use following code:
<code>from types import MethodType, FunctionType

class A(object):  # old style class
    def f(self): 
        return 42

def get_static_method(class_, method_name):
    return getattr(class_, method_name)

def make_unbound_method(func):
    return MethodType(FunctionType(func.im_func, func.im_self, func.im_class), None, None)

a = A()
f = make_unbound_method(get_static_method(a, 'f'))
print f()  # prints '42'
</code>
UPDATE2:
Python 3.4 adds a <code>MethodType.__init__</code> method, so you can do:
<code>def make_unbound_method(func):
    return MethodType.__init__(None, func.
