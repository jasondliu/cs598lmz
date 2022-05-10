import weakref

from gaphas.item import NW, NE, SE, SW, N, S, E, W
from gaphas.tool.tool import Tool
from gaphas.state import observed, reversible_pair
from gaphas.util import path_ellipse

from gaphor import UML
from gaphor.diagram.diagramtools import ToolHandle


class ConnectionHandle(ToolHandle):
    """
    Connection handle is used to connect items with each other.

    The handle consists of two parts:

        * A handle for dragging the connection point around;
        * A handle for changing the connection type (straight, orthogonal,
          polyline).
    """

    def __init__(self, element_factory, item, handle, connection, handle_index=0):
        ToolHandle.__init__(self, item, handle)
        self.element_factory = element_factory
        self.connection = connection
        self.handle_index = handle_index

    def draw(self, context):
        cr = context.cairo
        cr.set_line_width(
