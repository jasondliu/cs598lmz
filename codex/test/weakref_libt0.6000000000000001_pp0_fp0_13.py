import weakref

from .base import BaseProvider, BaseProviderPlugin
from .helpers import get_data_folder
from .helpers import get_data_file

from . import _providers
from . import _plugins


def register(cls, name=None):
    """Register a provider class.

    This function should be used as a decorator. The decorator should be
    applied to a provider class.

    The name argument is optional. If not given, the class name (with the
    module name stripped) will be used.
    """
    if name is None:
        name = cls.__name__
        if cls.__module__ != '__main__':
            name = cls.__module__ + '.' + name
    _providers[name] = cls
    return cls


def get_provider_class(name):
    """Get a registered provider class.

    This function will return the provider class with the given name. The name
    should be given as a string.
    """
    return _providers[name]


