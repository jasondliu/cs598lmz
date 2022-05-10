import weakref

from . import _ffi as ffi
from . import _lib as lib
from . import _api
from . import _signals
from . import _utils
from . import _types
from . import _text
from . import _vte
from . import _version

from . import _container
from . import _widget
from . import _window
from . import _application


class _VteTerminal(type):
    def __new__(cls, *args, **kwargs):
        if _version.vte_version < (0, 54, 0):
            # vte_terminal_set_input_enabled() was added in 0.54.0
            def set_input_enabled(self, enabled):
                pass
            def get_input_enabled(self):
                return True
            def set_input_enabled_async(self, enabled):
                pass
        else:
            def set_input_enabled(self, enabled):
                self._impl.set_input_enabled(enabled)
            def get_input_enabled(self):
                return self._impl
