fn = lambda: None
# Test fn.__code__.co_code
# fn.__code__.co_code
# Test fn.co_code
# fn.co_code
# Test ctypes.Array
# type(b'').__mro__
# Test special case with super class (object)

# class C(object):
#     def __getattr__(self, name):
#         return name
#
# c = C()
# Test metaclass

class MyMeta(type):
    def __getattr__(cls, name):
        return name

# class C(metaclass=MyMeta):
#     pass
# Test use 'super' with __getattr__


class GetattrSuper(object):
    def __getattr__(self, name):
        return super(GetattrSuper, self).__getattribute__(name)


# gs = GetattrSuper()
# Test use 'super' with __getattribute__


class GetattributeSuper(object):
    def __getattribute__(self, name):
        return super(GetattributeSuper, self).__getattr__(name)



