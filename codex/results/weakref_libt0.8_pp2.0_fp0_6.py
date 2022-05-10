import weakref

from lirc import RawConnection

__author__ = "Luka Pusic"
__version__ = "0.2.2"
__maintainer__ = "Luka Pusic"
__email__ = "luka@pusic.si"
__status__ = "Production"


class DecodeError(Exception):
    """Raised when decoding fails due to bad characters."""


class Callback(object):
    """A wrapper class used to pass callable attributes into this module."""
    def __init__(self, func, *args, **kwargs):
        """
        Create a Callback instance.

        :param func: A callable object.
        :type func: callable
        """
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        """
        Call the Callback instance.

        :param args: Extra positional arguments to pass to the callable.
        :param kwargs: Extra keyword arguments to pass to the callable.

