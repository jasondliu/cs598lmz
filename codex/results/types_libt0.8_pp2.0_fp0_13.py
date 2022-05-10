import types
types.MethodType(func, obj)

# Create unbound method
from types import MethodDescriptorType

def func(*args):
    print(args)

unbound_method = MethodDescriptorType(func)
unbound_method(1, 2, 3) #== func(1, 2, 3)

# Create static method
from types import StaticMethodType

def static_method(cls, *args):
    print(args)

static_method(1, 2, 3) #== static_method(1, 2, 3)

def method(cls, *args):
    print(args)

# Create class method
from types import ClassMethodType

ClassMethodType(method, 1)
# metaclass does the same
class Meta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return collections.OrderedDict()

# Create property
from types import PropertyType

def property_getter(self):
    return self._value

def property_setter(self, value):
   
