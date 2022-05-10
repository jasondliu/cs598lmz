import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class LazyStructField(object):
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        if instance is None:
            return self
        rv = self._get(instance)
        setattr(instance, self.name, rv)
        return rv
    def _get(self, instance):
        raise NotImplementedError(
            'This field cannot be accessed yet.'
        )

class LazyField(LazyStructField):
    def __init__(self, name, get_func):
        super(LazyField, self).__init__(name)
        self.get_func = get_func
    def _get(self, instance):
        return getattr(instance, self.get_func)()

class LazyArrayField(LazyField):
    def __init__(self, name, get_func, length_func):
        super(LazyArrayField, self).__init__(name, get_func)
        self.length_func = length
