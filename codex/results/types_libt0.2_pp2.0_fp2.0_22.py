import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# This is a hack to make the code compatible with Python 2.7
# and 3.x.
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from . import utils
from . import exceptions
from . import config
from . import constants
from . import validators
from . import fields
from . import schema
from . import query
from . import resources
from . import http
from . import pagination
from . import connection
from . import auth
from . import session
from . import client
from . import mapper
from . import transport
from . import middleware
from . import decorators
from . import version


__all__ = [
    'utils',
    'exceptions',
    'config',
    'constants',
    'validators',
    'fields',
    'schema',
    'query',
    'resources',
    'http',
    'pagination',
    'connection',
    'auth
