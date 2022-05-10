import weakref

from pymongo.errors import ConnectionFailure
from pymongo.read_preferences import ReadPreference
from pymongo.son_manipulator import (
    AutoReference,
    NamespaceInjector,
    ObjectIdInjector,
    ObjectIdShuffler,
)
from pymongo.son_manipulator import SONManipulator
from pymongo.write_concern import WriteConcern
from pymongo.cursor import Cursor, CursorType
from pymongo.helpers import _check_write_command_response
from pymongo.helpers import _is_command_cursor
from pymongo.helpers import _unpack_response
from pymongo.message import _COMMAND_OVERHEAD
from pymongo.monotonic import time as _time
from pymongo.pool import Pool
