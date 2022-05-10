import weakref

from . import _common
from . import _compat
from . import _data
from . import _errors
from . import _util
from . import _vendor

from . import _util as _u

from . import _vendor as _v

_log = _vendor.logging.getLogger(__name__)

_MAX_USER_ID = 2 ** 32 - 1

_MAX_GROUP_ID = 2 ** 32 - 1

_MAX_SIZE = 2 ** 63 - 1

_MAX_UID = 2 ** 32 - 1

_MAX_GID = 2 ** 32 - 1

_MAX_NANOSECONDS = 1e9

_MAX_DEV = 2 ** 32 - 1

_MAX_INO = 2 ** 64 - 1

_MAX_NLINK = 2 ** 32 - 1

_MAX_RDEV = 2 ** 32 - 1

_MAX_BLKSIZE = 2 ** 32 - 1

_MAX_BLOCKS = 2 ** 63 - 1

_MAX_FLAGS = 2 ** 32 - 1

_MAX
