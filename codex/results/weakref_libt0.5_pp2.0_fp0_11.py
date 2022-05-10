import weakref

import pygame

from . import constants
from . import image
from . import text
from . import events

from . import utils

class Widget(object):
    """
    Base class for all widgets.

    Widget objects are used to create UI elements for a pygame-gui app.
    Widgets can be used to display text, images and to capture user input.

    Widgets are organised into a tree structure. Each widget can have
    any number of child widgets. Child widgets are automatically positioned
    relative to their parent.

    Widgets can be created in python code, or via a xml file.

    A widget is created using the Widget() constructor. The constructor
    takes a number of parameters which can be used to set the initial
    properties of the widget.

    Widget properties can be set by assigning to the appropriate attribute.
    For example, to set the position of a widget use:

      widget.position = (x, y)

    Some widget properties can be set via a style dictionary. The style
    dictionary is specified as a keyword argument to the Widget() constructor.

    For example:


