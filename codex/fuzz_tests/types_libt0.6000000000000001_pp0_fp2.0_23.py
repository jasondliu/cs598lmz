import types
types.ClassType = type

try:
    import uuid
except ImportError:
    uuid = None

from roundup.exceptions import Reject
from roundup.cgi.exceptions import FormError
from roundup import hyperdb, date
from roundup.anypy.strings import b2s, s2b
from roundup.anypy import io, xmlrpc
from roundup.anypy.db_resources import DatabaseResources
from roundup.anypy.utils import ustr

# import the schema module
from roundup.hyperdb import schema

# import the properties module (for the possible property values)
from roundup.hyperdb import properties

# import the types module (for the possible property types)
from roundup.hyperdb import types

# import the boolean module (for the possible property boolean values)
from roundup.hyperdb import boolean

# Import the security module
from roundup.hyperdb import security


class HyperDatabase(hyperdb.Database):
    """
    A database with additional methods for use in the web interface

    This is used to access the data in a roundup instance. It provides
    methods for the web interface (as opposed
