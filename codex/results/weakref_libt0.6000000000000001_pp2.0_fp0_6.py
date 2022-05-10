import weakref
import functools
import threading

import numpy as np

from . import _pyglet
from . import gl
from . import clock
from . import event
from . import image
from . import resource
from . import font
from . import media
from . import sprite
from . import texture
from . import window

_have_pyopengl = False
try:
    from OpenGL import GL
    from OpenGL.GL import shaders
    from OpenGL.GL import framebufferobjects as FBO
    _have_pyopengl = True
except ImportError:
    pass

__all__ = ['Canvas', 'SceneGraph', 'mesh', 'shader', 'shaders', 'material',
           'BlendMode', 'Material', 'Color', 'MaterialGroup', 'Mesh',
           'VertexList', 'IndexedVertexList', 'VertexBuffer', 'IndexedVertexBuffer',
           'Batch', 'OrderedGroup', 'Group']

_debug_gl = False

def _debug_print(*args):
    if _debug_gl:
        print(*
