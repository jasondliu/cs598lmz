import gc, weakref
from wx.lib.floatcanvas import FloatCanvas
from wx.lib.floatcanvas.Utilities import BBox, Iterator

import Path, PathContour
try:
    from OpenGL.GL import *
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    openglcanvas = True
except:
    openglcanvas = False

from CNCRouterCommand import CNCRouterCommand, CNCRouterCommandType
import CNC
import Utils

USE_GL = True
MIN_SCALE = 10.0
MOUSE_CORRECTION = 1.0/10.0
MAX_VIEW_HISTORY = 10
class CNCRouterCanvas(FloatCanvas.FloatCanvas):
    def __init__(self, parent, grid, path_commands, show_backplot, use_opengl):
        FloatCanvas.FloatCanvas.__init__(self, parent)

        self.objectList           = []
        self._show_backplot       = show_backplot
        self._view_history        =
