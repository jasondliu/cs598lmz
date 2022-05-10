import gc, weakref
from . import types
from .exceptions import *
from . import core
from . import util
from . import _internal
from . import _internal2
from . import _internal3
from . import _internal4
from . import _internal5

from .core import *


try:
    from . import _internal6
except ImportError:
    pass
else:
    from . import _internal7


del _internal
del _internal2
del _internal3
del _internal4
del _internal5
del _internal6
del _internal7

from .types import *
from .core import *
from . import types
from . import core
del types
del core


try:
    from . import _internal6
except ImportError:
    pass
else:
    from . import _internal7


del _internal6
del _internal7

from .exceptions import *
from . import exceptions
del exceptions
if sys.version_info[0] >= 3:
    from . import _unicode
    del _unicode
else:
    from . import _unicode2
