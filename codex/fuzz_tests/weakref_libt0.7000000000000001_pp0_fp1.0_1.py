import weakref

from pyglet.event import EventDispatcher
import pyglet.graphics as graphics

from . import gl
from . import gl_state
from . import geometry
from . import glsl
from . import material
from . import render
from . import texture
from . import util
from . import vertex
from .vertex import VertexList

log = logging.getLogger(__name__)


class Node(EventDispatcher):
    """
    A node in a :class:`SceneGraph`.

    Nodes of the scene graph are arranged in a tree structure, with a root node
    at the top of the tree.  Nodes are arranged in a hierarchy for transforming
    their coordinates.  Each node has a local coordinate frame, and a global
    coordinate frame:

    * The local coordinate frame is relative to the parent node's local
      coordinate frame.
    * The global coordinate frame is relative to the root node's global
      coordinate frame.

    Child nodes inherit the transform of the parent node.

    The :func:`draw` function is called on each node to draw it.  This is
