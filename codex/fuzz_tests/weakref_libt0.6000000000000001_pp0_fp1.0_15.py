import weakref

# types
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Tuple

# mypy
from typing_extensions import Final

# mypy: allow-untyped-calls, allow-untyped-defs

# =============================================================================
#
# Globals
#
# =============================================================================

# =============================================================================
#
# Helpers
#
# =============================================================================

# =============================================================================
#
# Exceptions
#
# =============================================================================

# =============================================================================
#
# Callback
#
# =============================================================================

# =============================================================================
#
# CallbackManager
#
# =============================================================================


class CallbackManager:
    """
    A manager for callbacks.

    This class is used to manage callbacks for callback-based code.
    This class has methods for adding, removing, and running callbacks.
    """

    __slots__ = (
        "_callbacks",  # type: Final[Dict[str, Callable[..., None]]]
    )

    def __init__(self) -> None:
