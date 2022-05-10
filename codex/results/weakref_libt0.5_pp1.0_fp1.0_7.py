import weakref

from .. import core
from .. import events
from .. import exceptions
from .. import theme


class Widget(events.EventDispatcher):
    """A widget is the base class for all visible objects in urwid.

    Widgets can contain other widgets and define their own appearance
    and behaviour.  They can respond to user input, draw themselves on
    the screen, and arrange their child widgets.

    """

    #: True if this widget is selectable by the user.
    selectable = False

    #: True if this widget should be drawn in the focused state.
    focusable = False

    _sizing = frozenset(['box', 'flow', 'fixed', 'weight'])

    #: Default values for widget styling.
    #: See :ref:`theming-widgets` for more information.
    _selectable_defaults = dict(
        focus_attr='focus',
        focus_map={None: 'focus'},
        )
    _defaults = dict(
        cursor_position=0,
        )

    def __init__(self, *args, **
