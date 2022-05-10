fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16095: crash when __code__ is set to a non-code object
# that has a __call__ method.
class Callable:
    def __call__(self):
        pass

fn.__code__ = Callable()

# Issue #16095: crash when __code__ is set to a non-code object
# that has a __get__ method.
class Descriptor:
    def __get__(self, obj, objtype):
        pass

fn.__code__ = Descriptor()

# Issue #16095: crash when __code__ is set to a non-code object
# that has a __set__ method.
class NonDataDescriptor:
    def __set__(self, obj, value):
        pass

fn.__code__ = NonDataDescriptor()

# Issue #16095: crash when __code__ is set to a non-code object
# that has a __delete__ method.
class NonDataDescriptor:
    def __delete__(self, obj):
       
