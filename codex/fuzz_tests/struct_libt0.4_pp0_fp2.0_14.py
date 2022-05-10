import _struct

from . import _pycompat
from . import pycompat
from . import scmutil
from .i18n import _
from .node import hex, nullid, nullrev, short
from . import (
    error,
    obsolete as obsmod,
    pycompat,
    revlog,
    util,
)

packpfx = '%d\0' % len(revlog.packpfx)

# update flags
UF_UPDATE_FLAGS = 0xFFFF
UF_NOPREFLIGHT = 1 << 16
UF_ALLOW_UNRESOLVED = 1 << 17
UF_ALLOW_MISSING_SUCCESSOR = 1 << 18
UF_ALLOW_MISSING_SUCCESSOR_PREFLIGHT = 1 << 19
UF_ALLOW_MISSING_SUCCESSOR_NOPREFLIGHT = 1 << 20

# update return values
SUCCESS = 0
S_RETRY = 1
S_RESTART = 2
S_REDUNDANT = 3
S_OBSOLETE = 4
S
