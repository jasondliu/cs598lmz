import gc, weakref
from types import MethodType

from pyglet import gl
from pyglet.graphics import VertexList, draw
from pyglet.graphics import push_pop_projection_matrix, draw_indexed

from batch import VertexBatch, ReusableBatch, geometric_batches
from batch import FLOAT_SIZE, GLshort, GLushort, QUAD_INDICES, TRI_INDICES
from utils import flatten, cscaled, ft, cc
from utils import BoundProperty, SequenceProperty
from utils import uuid, ignore_exceptions, fc, tc, f_

from renderer import BaseRenderer, MultiObjectsRenderer, GroupRenderer
from renderer import EffectsRenderer
from shader import Shader
from geometry import Tesselable, Geometry, Polygon, Rectangle
from effect import Effect
from transform import Transformable
from texture import Texture


class Group(Transformable, SequenceProperty):

    renderer = GroupRenderer
    batch = geometric_batches

    parent = BoundProperty('parent')
    children = BoundProperty()
