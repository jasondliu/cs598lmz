import weakref

from . import _util


class _WeakMethod(object):
    """
    A weak reference to a bound method, working around the lifetime
    problem of bound methods.

    This class is necessary because a bound method has a reference to
    the instance it's bound to.  When the instance goes away, it's
    possible that we'll still have a reference to the bound method
    object lying around somewhere, such as in a list that we iterate
    over after the refcount on the instance goes to zero.  When this
    occurs, the __del__ method of the bound method will be called with
    a reference to the instance, which will cause the instance's __del__
    method to be called a second time.

    To work around this problem, we do two things:

    1.  We create a wrapper class whose sole purpose in life is to hold
        a weak reference to the bound method's instance.  When the
        weak reference dies, the wrapper is deleted, which breaks the
        reference loop.

    2.  We substitute our wrapper for the instance when creating the
        bound method.

    When we call the bound
