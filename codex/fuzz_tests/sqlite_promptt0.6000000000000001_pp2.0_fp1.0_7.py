import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared")

from OpenGL import constants, constant
from OpenGL.platform import PLATFORM
from OpenGL.error import GLError
from OpenGL.raw.GL.VERSION.GL_1_0 import *
from OpenGL.raw.GL.VERSION.GL_1_1 import *
from OpenGL.raw.GL.VERSION.GL_1_2 import *
from OpenGL.raw.GL.VERSION.GL_1_3 import *
from OpenGL.raw.GL.VERSION.GL_1_4 import *
from OpenGL.raw.GL.VERSION.GL_1_5 import *
from OpenGL.raw.GL.VERSION.GL_2_0 import *
from OpenGL.raw.GL.VERSION.GL_2_1 import *
from OpenGL.raw.GL.VERSION.GL_3_0 import *
from OpenGL.raw.GL.VERSION.GL_3_1 import *
from OpenGL.raw.GL.VERSION.GL_3_2 import *
from OpenGL.raw.GL.VERSION.GL_3_3 import *
from OpenGL.raw.GL.VERSION.GL_4_
