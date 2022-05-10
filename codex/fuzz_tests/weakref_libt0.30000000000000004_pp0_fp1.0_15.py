import weakref

from . import _core
from . import _util
from . import _widget
from . import _window

__all__ = [
    "Button",
    "CheckBox",
    "ColorSelector",
    "ComboBox",
    "DateTimePicker",
    "Dialog",
    "DropDown",
    "FilePicker",
    "FileSelector",
    "ImageView",
    "Label",
    "ListBox",
    "MenuBar",
    "MessageDialog",
    "Popup",
    "ProgressBar",
    "RadioButton",
    "ScrollBar",
    "Slider",
    "SpinBox",
    "TextBox",
    "TextEdit",
    "ToolButton",
    "Tree",
    "Window",
]


class Button(_widget.Widget):
    """
    A button widget.

    Parameters
    ----------
    label : str, optional
        The button label.
    icon : str, optional
        The icon name.
    on_click : callable, optional
        The callback to execute when the
