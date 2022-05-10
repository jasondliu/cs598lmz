import gc, weakref
from . import _core
from . import _core as core
from . import _internal
from . import _internal as internal
from . import _util
from . import _util as util
from . import _widget
from . import _widget as widget
from . import _window
from . import _window as window

class Edit(widget.Widget):
    """
    Edit widget

    :param parent: the parent window. Must not be None
    :param rect: an object with left, top, width and height attributes
    :param text: the initial text
    :param style: the style. Can be None to use the default style.
    :param autotab: if True, pressing the Tab key will switch to the next widget
    :param multiline: if True, the widget will accept multiple lines
    :param password: if True, the widget will display a password
    :param readonly: if True, the widget will be read-only
    :param align: the horizontal text alignment
    """
    def __init__(self, parent, rect, text, style=None, autotab=False, multiline
