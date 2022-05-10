import gc, weakref, sys, os

#-------------------------------------------------------------------------------

class WeakCallback(object):
    """
    A callback that can be registered with a weak reference.
    """
    def __init__(self, callback, *args, **kwargs):
        """
        Constructor.

        @param callback: The callback to be called.
        @param args: The arguments to be passed to the callback.
        @param kwargs: The keyword arguments to be passed to the callback.
        """
        self.__callback = callback
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self):
        """
        Call the callback.
        """
        self.__callback(*self.__args, **self.__kwargs)

#-------------------------------------------------------------------------------

class WeakMethod(object):
    """
    A method that can be registered with a weak reference.
    """
    def __init__(self, method):
        """
        Constructor.

        @param method: The method to be called.
        """
        self.__method = method

    def __
