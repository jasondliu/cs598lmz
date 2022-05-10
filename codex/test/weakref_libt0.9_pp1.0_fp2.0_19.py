import weakref
import multiprocessing
import random
import pyopengl
from contextlib import contextmanager


from . import tasks, graphics, utils
from . import graphics_constants, blobs_constants
from .utils import logger


def _get_view():
    import melissilolg.views
    return melissilolg.views.View()


class _EglConfigObject:
    double_buffering = 1
    depth_size = 16
    stencil_size = 0
    red_size = 8
    green_size = 8
    blue_size = 8
    alpha_size = 8
    multisampling = 0
    draw_method = None


class ViewConfiguration:
    def __init__(self):
        self.egl_attrs = _EglConfigObject()
        self.egl_attrs.draw_method = pyopengl.EGL_DRAW
        self.view_transform = Matrix4()
        self.viewport_transform = Matrix4()


