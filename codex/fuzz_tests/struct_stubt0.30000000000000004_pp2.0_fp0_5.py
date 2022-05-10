from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# Descriptors
class Descriptor(object):
    def __get__(self, obj, objtype):
        print 'Descriptor.__get__'
        return 1

class DescriptorClass(object):
    descriptor = Descriptor()

DescriptorClass.descriptor

# Slots
class SlotsClass(object):
    __slots__ = ['a', 'b']
    def __init__(self):
        self.a = 1
        self.b = 2

s = SlotsClass()
s.a
s.b

# Weakref
import weakref
class WeakrefClass(object):
    pass

w = weakref.ref(WeakrefClass())
w()

# Weakref callback
def callback(obj):
    print 'callback'

w = weakref.ref(WeakrefClass(), callback)
w()

# Weakref proxy
class WeakrefClass(object):
    def __init__(self):
        self.a = 1
