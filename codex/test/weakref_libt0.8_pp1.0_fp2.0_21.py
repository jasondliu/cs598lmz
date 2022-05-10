import weakref

from typing import Callable, List

from pyglet.window.key import KeyStateHandler

from arcade.gui.elements import UIElement
from arcade.gui.text_box import TextBox
from arcade.gui.ui_style import UIStyle
from arcade.gui import UIManager

__all__ = ["UIKeyboardEventHandler"]


class UIKeyboardEventHandler:
    """
    UIKeyboardEventHandler supports the mapping of keyboard events to ui
    elements. This class supports two different methods of keyboard focus:

        1. The inactive-next-active method, where focus is passed to the next
           element. This is the default method.
        2. The click-to-focus method, where an element must be clicked on
           to take focus.

    To use the click-to-focus method, call set_click_to_focus before
    adding any elements.
    """

