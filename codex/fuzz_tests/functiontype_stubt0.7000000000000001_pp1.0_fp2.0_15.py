from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x:x))
print(type((x for x in [1])))
print(type(iter([])))
print(type(None))
print(type(int))
print(type(type),type(type) == type)

import os
print(type(os))

print(isinstance(int,type))
print(isinstance(int,object))
print(isinstance(int,FunctionType))
print(isinstance(int,type))

print(dir(int))

print(getattr(int,'__name__'))
setattr(int,'name','int')
print(getattr(int,'name'))

print(int.__bases__)

# __bases__ is a tuple of base classes
# __class__ is the instance's class
# type(instance_or_class) is the instance's or class' type
# isinstance(instance, class_or_type) is True if the instance's class is subclass of the class_or_type
# issub
