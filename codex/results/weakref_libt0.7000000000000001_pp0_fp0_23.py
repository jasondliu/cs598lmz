import weakref
from typing import List

import pygame

from ui.constants import (
    Color,
    Font,
    Layout,
    Theme,
)
from ui.elements.element import Element, Label
from ui.elements.selector import Selector
from ui.elements.text_box import TextBox
from ui.elements.tooltip import Tooltip
from ui.utils.exceptions import InvalidChoiceException


class Dropdown(Element):
    """
    A dropdown list of possible choices. It has a primary label that is always
    displayed, and a secondary label that is displayed only when the dropdown
    is active.

    :param theme: the theme to use for this dropdown
    :param options: the list of possible choices
    :param initial_value: the initial value
    :param initial_index: the initial value as an index into options
    :param tooltip: the tooltip to display when hovering over this element
    """
    def __init__(
            self,
            theme: Theme,
            options: List[str],
            initial_value:
