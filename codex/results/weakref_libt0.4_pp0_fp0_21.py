import weakref

from . import _base


class WeakMethod(_base.WeakMethod):
    """Weak reference to a method.

    This is a subclass of :class:`weakref.WeakMethod` that adds a
    :meth:`__call__` method.

    """

    def __call__(self, *args, **kwargs):
        """Invoke the method.

        If the target is no longer alive, :exc:`ReferenceError` is raised.

        """
        return self.__call__(self, *args, **kwargs)


class WeakMethodProxy(_base.WeakMethodProxy):
    """Weak reference to a method.

    This is a subclass of :class:`weakref.ProxyType` that adds a
    :meth:`__call__` method.

    """

    def __call__(self, *args, **kwargs):
        """Invoke the method.

        If the target is no longer alive, :exc:`ReferenceError` is raised.

        """
        return self.__call__(self, *args, **kwargs)
