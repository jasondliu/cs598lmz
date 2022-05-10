import _struct

from uio import BytesIO

from ..ffi import ffi
from ..ffi import C
from .error import Error
from .error import FSError
from .error import MemoryError
from .error import InvalidArgumentError
from .error import UnsupportedError
from .error import NotImplementedError
from .error import UnsupportedTokenError

from .constants import DEFAULT_FSEXPORT_FORMAT
from .constants import libarchive_version_major
from .constants import libarchive_version_minor
from .constants import libarchive_version_string
from .constants import libarchive_version_number

from .constants import ARCHIVE_EOF
from .constants import ARCHIVE_OK
from .constants import ARCHIVE_RETRY
from .constants import ARCHIVE_WARN
from .constants import ARCHIVE_FAILED
from .constants import ARCHIVE_FATAL

from .constants import ARCHIVE_EOF
from .constants import ARCHIVE_OK
from .constants import ARCHIVE
