import weakref

from . import base
from . import events
from . import interfaces
from . import utils
from . import _compat as compat
from . import _event
from . import _utils
from . import _widgets
from . import _widgets_base


class _Base(base.Widget):
    """Base class for all widgets."""

    _widget_type = None

    def __init__(self, parent, *args, **kwargs):
        super(_Base, self).__init__(parent, *args, **kwargs)
        self._create()

    def _create(self):
        self._impl = self._create_impl()
        self._impl._set_widget(self)
        self._impl.create()

    def _create_impl(self):
        return self._toolkit.create_widget(self._widget_type, self)

    def _get_impl(self):
        return self._impl

    def _set_impl(self, impl):
        self._impl = impl
        self._impl._set_widget(self)

    impl = property(_
