import gc, weakref
from ctypes import *
from OpenGL.platform import PLATFORM as _p
from OpenGL import _util, arrays
from OpenGL._bytes import as_8_bit
from OpenGL.platform.baseplatform import BasePlatform as _b
from OpenGL import error
from OpenGL.raw._GLES3 import _types
from OpenGL.raw._GLES3.raw.GLES3 import *
from OpenGL.raw._GLES3.raw._constants import *


from OpenGL.lazywrapper import lazy as _lazy
from OpenGL.extensions import alternate
from OpenGL.extensions import alternateMethods as _alt

from OpenGL.raw._GLES3.GLES3 import _simple as simple
from OpenGL.raw._GLES3 import _errors as _error

from OpenGL.raw._GLES3.raw._types import _GLES3 as types
from OpenGL.raw._GLES3.raw._types import (
    GLbitfield, GLboolean, GLbyte, GLchar, GLclampd, GLclampf, GLdouble, 
    GLeglImageOES, GLenum, GLfloat, GLhalf, GLhalf
