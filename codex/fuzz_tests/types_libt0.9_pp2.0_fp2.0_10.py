import types
types.MethodType(delattr, obj, 'x')

# Make sure we can call these methods...
obj.__str__()
obj.__unicode__()
obj.__class__()
obj.__cmp__(obj)
obj.__hash__()
obj.__nonzero__()
obj.__delattr__('x')
obj.__getattribute__('x')
obj.__setattr__('x', 42)
obj.__getattribute__('x')
obj.__delattr__('x')

obj.__str__()
obj.__unicode__()
obj.__class__()
obj.__cmp__(obj)
obj.__hash__()
obj.__nonzero__()
obj.__delattr__('x')
obj.__getattribute__('x')
obj.__setattr__('x', 42)
obj.__getattribute__('x')
obj.__delattr__('x')

#
# The eval function has several different attributes that control the
# environment in which the code is executed.  These are:
#
# - __built
