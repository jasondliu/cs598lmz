import weakref
import builtins

from ..constants import *
from ..api import api_method
from ..api import api_return

from ..core.log import getLogger

from .element import Element

# from .selectors.selector import Selector
# from .selectors.selectorall import SelectorAll
# from .selectors.selectorone import SelectorOne

log = getLogger(__name__)

class Document(Element):
    """
    Document represents the entire HTML document.
    """

    def __init__(self, page):
        super().__init__()
        self._page = weakref.ref(page)
        self._script_context = page.script_context

    def __getattr__(self, key):
        """
        Custom attribute getter which allows the Document to return
        Element objects for the following automatically-generated
        attributes:

        - getElementById
        - getElementsByName
        - getElementsByTagName
        - getElementsByClassName
        """
        return Element(self._page(), self._script_
