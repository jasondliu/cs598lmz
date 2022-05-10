import gc, weakref
from weakref import proxy
from collections import OrderedDict

from pyglet.gl import *
from pyglet import clock
from pyglet.window import key

from euclid import Vector2, Point2, Vector3, Point3
from math import sin, cos, pi, floor, sqrt, isnan, radians

from gamelib.constants import (
    DEBUG,
    DEBUG_OUTPUT,
    DEBUG_COLLISION,
    DEBUG_DRAW_POINT,
    DEBUG_DRAW_AABB,
    DEBUG_DRAW_CIRCLE,
    DEBUG_DRAW_COLLIDERS,
    DEBUG_DRAW_TILE_COLLIDERS,
    DEBUG_DRAW_SUBDIVISION,
    DEBUG_DRAW_NORMALS,
)

from gamelib.util import (
    clamp,
    bounding_box,
    bounding_box_from_points,
    init_opengl,
    distance,
    distance_sq,
    aabb_collision,
    shuffled,
