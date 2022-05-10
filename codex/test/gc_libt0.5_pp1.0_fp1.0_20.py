import gc, weakref, inspect

def weak_method(func):
    """
    Return a weak reference to a bound method.

    Parameters
    ----------
    func : method
        A bound method

    Returns
    -------
    weakref
        A weak reference to the bound method
    """
    return weakref.WeakMethod(func)


def weak_instancemethod(func):
    """
    Return a weak reference to a bound instancemethod.

    Parameters
    ----------
    func : instancemethod
        A bound instancemethod

    Returns
    -------
    weakref
        A weak reference to the bound instancemethod
    """
    return weakref.WeakMethod(func)


def weak_function(func):
    """
    Return a weak reference to a function.

    Parameters
    ----------
    func : function
        A function

    Returns
    -------
    weakref
        A weak reference to the function
    """
    return weakref.ref(func)


