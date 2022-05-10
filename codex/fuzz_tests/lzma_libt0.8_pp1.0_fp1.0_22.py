import lzma
lzma.open = lzma.LZMAFile
from io import open
import sys
from io import BytesIO
from . import util
from . import exceptions
from . import compat
from . import file_io
from .entry import BaseEntry
from . import link
from . import operation_factory
from . import operation_types as types
from .permissions import Permissions
from .volume import Volume
from .progress import Progress
from .operation_modifiers import OperationModifiers

if sys.version_info[0] > 2:
    _unicode = str
else:
    _unicode = unicode


class Archive(util.LegacyArchiveInterface):
    """Major interface to working with archives.

    You can create Archive instances in two ways:

    1. Call :func:`py7zr.SevenZipFile` factory function::

        >>> from py7zr import SevenZipFile
        >>> archive = SevenZipFile('foo.7z', mode='w')

    Will create a new archive.

    2. Call :class:`py7zr.archive.Archive` constructor::
