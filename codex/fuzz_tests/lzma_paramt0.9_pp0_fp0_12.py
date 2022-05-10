from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor  # noqa
from lzma import open as lzma_open  # noqa
from lzma import open as lzma_compat_open  # noqa

from .compat import BytesIO
from .compat import DEV_NULL
from .compat import FileExistsError
from .compat import PermissionError
from .compat import PIP_VERSION
from .compat import SameFileError
from .compat import TemporaryDirectory
from .compat import UnsupportedOperation

from .constants import ArgType
from .constants import COMMON_PY_VERSIONS
from .constants import DEFAULT
from .constants import F_OK
from .constants import Permission
from .constants import PIP_DELETE_MARKER_FILENAME


class EnvPathLib(object):
    """Wrappers around common path operations."""

    def realpath(self, path):
        """Get the canonical path of the specified filename, eliminating any
        symbolic links encountered in the path."""
        return os.path.realpath
