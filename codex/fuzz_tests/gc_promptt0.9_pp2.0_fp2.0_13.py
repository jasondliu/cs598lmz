import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#gc.collect() should not effect weakref lists

gc.set_debug(gc.DEBUG_LEAK | gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)


def fatal(msg):
    raise RuntimeError, msg

# A list of callbacks is kept for callbacks that are easier to write
# as functions.  Callbacks added to this list will not prevent
# objects from being collected.  The callbacks are called with no
# arguments.
global _callback_weaklist
_callback_weaklist = []

# Create an instancemethod object, outside of a class definition, with
# a __del__ method that adds a callback to _callback_weaklist
im = type.__dict__['__new__'](type(lambda:0), lambda:0, {},
                   {'__del__': lambda: _callback_weaklist.append(None)})
# Convert a function to an instancemethod
import new
im2 = new.instancemethod(lambda x: id(x), None, im)
# Write the instancemethod into a slot of an instance
class C
