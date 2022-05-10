import types
types.small_int_ranges = range(-5,257)

def method_getattr(self, name):
    try:
        return self.__methods__[name]
    except KeyError:
        raise AttributeError, name

def method_setattr(self, name, value):
    self.__methods__[name] = value

def new_method_type(name, bases, dict):
    dict.__methods__ = {}
    dict.__getattr__ = method_getattr
    dict.__setattr__ = method_setattr
    return types.new_class(name, bases, dict)

types.MethodType = new_method_type('instancemethod',
                                   (object,),
                                   {'__new__': new_instancemethod})

def method_is_true(self):
    return self.__self__ is not None

types.MethodType.__nonzero__ = method_is_true


#------------------------------------------------------------------------
# test
#------------------------------------------------------------------------

def test():
    class C:
        def f(self, x=
