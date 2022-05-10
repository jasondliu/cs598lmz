import select
import socket
import sys
import time
import traceback

from . import _common
from . import _constants
from . import _util
from . import _util_posix
from . import _util_windows
from . import _winapi


class _SelectorKey(_common.SelectorKey):
    """A key returned by `selectors.Selector.select()`.

    This class is intended to be private to the `selectors` module.

    """
