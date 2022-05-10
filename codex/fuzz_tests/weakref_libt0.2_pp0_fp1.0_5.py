import weakref

import numpy as np

from . import _pyglet
from . import gl
from . import clock
from . import event
from . import image
from . import resource
from . import window
from . import app
from . import font
from . import glu
from . import graphics
from . import sprite
from . import text
from . import media
from . import view
from . import util
from . import compat_platform

_debug_gl = False

_debug_trace_gl = False

_debug_trace_gl_dump = False

_debug_trace_gl_path = None

_debug_trace_gl_start = None

_debug_trace_gl_end = None

_debug_trace_gl_ignore = set()

_debug_trace_gl_ignore_paths = set()

_debug_trace_gl_ignore_modules = set()

_debug_trace_gl_ignore_objects = set()

_debug_trace_gl_ignore_filters = set()

_debug_trace_gl_ignore_args = set()
