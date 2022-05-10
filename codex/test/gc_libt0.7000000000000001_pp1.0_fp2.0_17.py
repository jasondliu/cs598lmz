import gc, weakref

import faulthandler
faulthandler.enable()

#===============================================================================
# Test the gc module.
#===============================================================================

# The following is a list of callbacks set by calling gc.callbacks.set.  When
# gc.collect() is called, these callbacks are called.  Note that callbacks are
# called in the reverse order of the order in which they were registered.

# Callbacks are called with one argument, the phase, which will be one of the
# following:

#     0: The collection of unreachable objects has begun.
#     1: The collection of unreachable objects is complete.

# Note that the callbacks can be called several times for the same collection
# if the collection is aborted and restarted.

# Note that it is possible to cause a callback to be registered more than
# once by calling gc.callbacks.set multiple times with the same function.
# The duplicate callbacks will be called in the reverse order of their
# registration.

# When a callback is called, it is removed from the list of registered
# callbacks
