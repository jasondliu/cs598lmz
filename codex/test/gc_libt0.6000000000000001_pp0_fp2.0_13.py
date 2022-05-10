import gc, weakref

# The following classes are for internal use only.

class _weakmethod(object):
    # a slot wrapper for a weak reference to a bound method
    # an instance of this class is created for each weakly referenced
    # bound method that lives more than one iteration of the garbage
    # collector

    __slots__ = '_func', '_meth', '_cls'

    def __init__(self, func, meth, cls):
        # func is a function object
        # meth is a descriptor or a slot wrapper for a bound method
        # cls is a class object

        self._func = func
        self._meth = meth
        self._cls = cls

    def __call__(self):
        # return a new instance of the original bound method
        # or the original function if referral is dead

        func = self._func
        if func is None:
            raise ReferenceError('weakly referenced object no longer exists')

        meth = self._meth
