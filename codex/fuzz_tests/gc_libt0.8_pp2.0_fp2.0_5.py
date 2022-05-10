import gc, weakref

from . import _reflow
from .log import debug, info
from .errors import ParsingError, InvalidValue
from . import css


def _hx_repr(self):
    return "%s(%s)" % (self.__class__.__name__, repr(self.element)[1:-1])

class element(object):
    """
    Parsing of DOM elements, including style information
    """
    def __init__(self, element, check_value, get_style, default_style):
        """
        Initialise element
        """
        self.element = element
        self.check_value = check_value
        self.get_style = get_style
        self.default_style = default_style
        self.__repr__ = _hx_repr
        self.children = [element(c, check_value, get_style, default_style)
                         for c in element]
        self.base = 'http://xml.zeit.de'
        self.position = 0
        self.left = 0
        self.top =
