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


