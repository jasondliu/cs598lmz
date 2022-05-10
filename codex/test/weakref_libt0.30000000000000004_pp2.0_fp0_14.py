import weakref

from . import _core
from . import _util
from . import _widgets
from . import _window

__all__ = [
    'App',
    'AppContext',
    'AppLoop',
    'AppLoopEvent',
    'AppLoopEventType',
    'EventLoop',
    'EventLoopPolicy',
    'EventLoopPolicyType',
    'Window',
    'WindowConfig',
    'WindowEvent',
    'WindowEventType',
    'WindowState',
    'WindowStateEvent',
    'WindowStateEventType',
    'WindowStyle',
    'WindowStyleEvent',
    'WindowStyleEventType',
]

# ------------------------------------------------------------------------------
# EventLoopPolicyType
# ------------------------------------------------------------------------------


class EventLoopPolicyType(enum.Enum):
    """
    The type of the event loop policy.

    The event loop policy determines how the event loop is created.
    """
