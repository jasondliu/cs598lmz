import weakref

from . import _compat as _
from . import errors as _errors
from . import util as _util
from . import config as _config
from . import log as _log
from . import _pycompat as _pycompat
from . import _uimod as _uimod
from . import _uimod_qt as _uimod_qt
from . import _uimod_gl as _uimod_gl
from . import _uimod_wx as _uimod_wx
from . import _uimod_tk as _uimod_tk
from . import _uimod_gtk as _uimod_gtk
from . import _uimod_gtk3 as _uimod_gtk3

# -----------------------------------------------------------------------------
# Exceptions
# -----------------------------------------------------------------------------

class UIError(Exception):
    """Base class for all UI-related errors."""

class UINotSupportedError(UIError):
    """Raised when a UI is not supported on the current platform."""

