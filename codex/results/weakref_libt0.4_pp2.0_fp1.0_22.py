import weakref
from collections import namedtuple
from contextlib import contextmanager

from . import _compat, _config, _constants, _errors, _util
from . import _types, _utils
from .client import Client
from .collection import Collection
from .cursor import Cursor
from .database import Database
from .encryption import ClientEncryption
from .encryption_options import ClientEncryptionOptions
from .gridfs import GridFSBucket
from .read_concern import ReadConcern
from .read_preferences import ReadPreference
from .write_concern import WriteConcern

try:
    import ssl
except ImportError:
    ssl = None

try:
    from bson.py3compat import integer_types
except ImportError:
    integer_types = int

try:
    from bson.py3compat import string_type
except ImportError:
    string_type = str

try:
    from bson.py3compat import string_types
except ImportError:
    string_types = str

try:
    from bson.
