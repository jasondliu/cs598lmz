import gc, weakref
import errno
from contextlib import ExitStack
from collections import defaultdict

from .fsencoding import (
    path_to_unicode,
    path_to_bytes,
    path_to_bytes_and_check,
    unicode_to_path,
    bytes_to_path,
    )

from . import (
    debug,
    errors,
    fileinfo,
    i18n,
    safe_hasattr,
    )

from .i18n import (
    gettext as _,
    ngettext,
    )

from . import (
    ignore,
    pathmatch,
    )

class Snapshot(object):
    """A snapshot of a directory.

    This is an abstract base class.  Subclasses provide different
    implementations.

    Not all APIs are available in all types of snapshots.  A subclass
    should provide enough information so that callers know what APIs
    to use.

    """

    def __init__(self, name=None):
        """Create a new snapshot instance.
        """
        self.
