import types
types.new_class(cls0)
cls = types.new_class(cls0)

# dynamically injecting a base class in the class dict, which triggers
# __new__ inheritance cache miss, which then triggers a cache miss when
# trying to call the __init_subclass_with_meta__
# (related to https://github.com/python/cpython/issues/22193)
import sys
cls.__class__.__setitem__(cls, '__bases__', (cls0, ))
cls.__init_subclass_with_meta__

# this one passes all asserts in DebugBuild, but does not call the method with OptBuild
# for some reason the __new__ of cls0 is not being called during ``type.__new__(...)``
import types
types.new_class(cls)
cls = types.new_class(cls)

# this one is a variation of the first one, except we add the base class
# to the __bases__ tuple after the class has been created and the
# __init_subclass_with_
