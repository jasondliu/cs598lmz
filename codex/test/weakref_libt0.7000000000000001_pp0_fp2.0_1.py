import weakref

def weak_callback(source, func, *args, **kwargs):
    """A wrapper for weak references to bound methods.

    Replace a bound method with a function that checks if the
    referenced object (an instance of some class) still exists, and
    calls the bound method if it does.

    The signature for this function is the same as a callback: it
    takes two arguments, a reference to the object, and a positional
    argument list.
    """

    # Check if the weak reference is dead
    if source() is None:
        return

    # Check if the function is dead
    if func.__self__() is None:
        return

    # Callable objects are (hopefully) still alive, so call the
    # callback
    func(*args, **kwargs)

