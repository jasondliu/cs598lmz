import ctypes
ctypes.cast(0, ctypes.py_object)

class FirstClass(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.value)

class SecondClass(FirstClass): pass

class ThirdClass(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.value)

class FourthClass(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.value)

f = FirstClass(1)
s = SecondClass(2)
t = ThirdClass(3)
u = FourthClass(4)

def distinguish_classes(instance, class_list):
    v =
