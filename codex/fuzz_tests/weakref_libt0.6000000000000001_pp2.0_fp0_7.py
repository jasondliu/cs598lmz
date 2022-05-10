import weakref

from gaphor.core.modeling import Presentation
from gaphor.core.modeling.mixins import NameOwned, NamedElement, Element

class Diagram(Element, NameOwned):
    """Class representing a diagram.

    This diagram contains all the graphical elements, like lines and boxes.
    """

    def __init__(self, id=None, name=None):
        """Initialize a new diagram.

        When an id is provided, the diagram is registered in the
        global diagram service.
        """
        super(Diagram, self).__init__(id, name)
        self.canvas = None

    def update_presentation(self, parent):
        """Update the presentation for a diagram.

        The presentation is the canvas part of the diagram.  The
        parent is the parent canvas item.
        """
        self.canvas = Canvas(parent, self)


class Canvas(Presentation):
    """This class contains all the graphical elements of a diagram.

    It is the canvas in which the diagram is drawn.
    """

    def __init__
