import types
types.MethodType(lambda self: None, None, D)

# test __new__
class E(object):
    def __new__(cls):
        return object.__new__(cls)
E()

# test __init__
class F(object):
    def __init__(self):
        pass
F()

# test __del__
class G(object):
    def __del__(self):
        pass
G()

# test __getattr__
class H(object):
    def __getattr__(self, name):
        pass
H().x

# test __setattr__
class I(object):
    def __setattr__(self, name, value):
        pass
I().x = 42

# test __delattr__
class J(object):
    def __delattr__(self, name):
        pass
del J().x

# test __getattribute__
class K(object):
    def __getattribute__(self, name):
        pass
K().x

# test __get__
class L(object
