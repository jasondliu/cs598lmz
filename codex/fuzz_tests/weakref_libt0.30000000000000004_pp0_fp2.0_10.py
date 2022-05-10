import weakref

from . import _compat as six
from . import _utils as utils
from . import _wrappers as wrappers


class ObjectProxy(object):
    """
    A proxy for another object.

    This is a base class for proxies that wrap objects.
    """

    __slots__ = ('__wrapped__',)

    def __init__(self, wrapped):
        """
        Initialize the proxy.

        :param wrapped: The object to wrap.
        """
        self.__wrapped__ = wrapped

    def __getattr__(self, name):
        """
        Get an attribute from the wrapped object.

        :param name: The name of the attribute.
        :return: The value of the attribute.
        """
        return getattr(self.__wrapped__, name)

    def __setattr__(self, name, value):
        """
        Set an attribute on the wrapped object.

        :param name: The name of the attribute.
        :param value: The value of the attribute.
        """
        if name in self.__slots__:
