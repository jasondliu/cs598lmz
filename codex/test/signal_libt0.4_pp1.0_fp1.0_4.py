import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtOpenGL
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from ui_mainwindow import Ui_MainWindow

import math
import numpy

from lib.math3d import *
from lib.shapes import *

from lib.gl_utils import *
from lib.gl_utils import _assert
from lib.gl_utils import _print
from lib.gl_utils import _error

from lib.gl_utils import gl_init
from lib.gl_utils import gl_init_texture
from lib.gl_utils import gl_init_vertex_array
from lib.gl_utils import gl_init_framebuffer
