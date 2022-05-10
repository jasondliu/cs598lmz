import weakref

from . import _base
from . import _compat
from . import _util
from . import _vendor
from . import _wrappers
from . import exceptions
from . import interfaces
from . import util
from . import _compat
from . import _util
from . import _wrappers
from . import exceptions
from . import interfaces
from . import util

_marker = object()

class _AdapterRegistry(_base._AdapterRegistry):
    """ A registry that adapts objects to one interface
    """
    def __init__(self):
        self.factories = {}

    def register(self, required, provided, name='', info=''):
        """ Register an adapter factory

        o 'required' must be a tuple of interfaces or classes or
          a single interface or class (not None).

        o 'provided' must be an interface or class (not None).

        o 'name' should be the name of the adapter factory.

        o 'info' should be a doc string or other useful information
          about the factory.
        """
