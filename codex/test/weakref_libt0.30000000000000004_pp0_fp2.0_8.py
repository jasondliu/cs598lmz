import weakref

from . import _core
from . import _util

from . import _event
from . import _event_loop
from . import _event_loop_policy
from . import _events
from . import _exceptions
from . import _futures
from . import _log
from . import _overrides
from . import _platform
from . import _signals
from . import _tasks
from . import _traceback
from . import _typing
from . import _weakref

from . import _debug

from . import _test

from . import _version

__version__ = _version.__version__

# This symbol is meant to be imported by third-party modules that want to
# be compatible with asyncio as it evolves.
# It will change in backward incompatible ways when asyncio's internals
# (e.g. the event loop policy) change in a way that affects the API.
#
# For example, if a new event loop policy is added that changes the
# behavior of get_event_loop(), then the API_VERSION will be bumped.
#
# The API
