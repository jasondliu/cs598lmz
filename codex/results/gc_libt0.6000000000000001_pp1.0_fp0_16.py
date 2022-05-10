import gc, weakref
import numpy
from numpy import *
import numpy.linalg as la

from pyglet.gl import *

from pyglet import image
from pyglet.gl import gl_info

import glsl

from ctypes import c_void_p

from pymorph import util

def _with_context(f):
    def g(*args, **kw):
        context = gl_info.get_current_context()
        if not context:
            config = Config()
            context = config.create_context(None)
        return f(context, *args, **kw)

    return g

def _define_basic_types():
    # Define basic types
    # FIXME: Support ctypes.Structure and ctypes.Union
    for name, ctype in [
        ('int8', c_byte),
        ('uint8', c_ubyte),
        ('int16', c_short),
        ('uint16', c_ushort),
        ('int32', c_int),
        ('uint32', c_uint),
       
