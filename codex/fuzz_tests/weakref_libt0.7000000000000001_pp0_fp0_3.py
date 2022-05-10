import weakref
from .element import Element, ElementPath
from .rect import Rect
from .text import Text
from .image import Image
from .animation import Animation
from . import event, tools, _compat
from . import _compat, tools

class Container(Element):
    """
    A Container is a special Element that is able to contain other Elements. You
    can add, remove and clear Elements from it.

    All containers have a position and a size. The size is determined by the
    position of the containing Elements. The position, however, is determined by
    the parent container.

    Containers are also :class:`Element` instances, and can therefore be added to
    other containers.
    """

    def __init__(self, parent=None, width=None, height=None):
        """
        :param parent: The parent container
        :type parent: :class:`Container`
        :param int width: The width of the container, in pixels
        :param int height: The height of the container, in pixels
        """
        super(Container, self).__init__(parent=parent)

