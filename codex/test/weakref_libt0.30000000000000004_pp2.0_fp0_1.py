import weakref

from . import _core
from . import _util
from . import _window
from . import _widget

class _TextFieldBase(_widget.Widget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._on_change = _util.Event()
        self._on_return = _util.Event()
        self._on_text_change = _util.Event()

    def _configure(self, **kwargs):
        super()._configure(**kwargs)

        self._on_change = _util.Event()
        self._on_return = _util.Event()
        self._on_text_change = _util.Event()

    @property
    def on_change(self):
        """
        Event that is triggered when the text field is changed.
        """
        return self._on_change

    @property
    def on_return(self):
        """
        Event that is triggered when the user presses the return key.
        """
        return self._on_return
