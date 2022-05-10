import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from . import utils

#-------------------------------------------------------------------------------
#   Some constants
#-------------------------------------------------------------------------------

# Default color for the background of the canvas
DEFAULT_BG_COLOR = QColor(255, 255, 255)

# Default color for the foreground of the canvas
DEFAULT_FG_COLOR = QColor(0, 0, 0)

# Default size for the canvas
DEFAULT_CANVAS_SIZE = (512, 512)

# Default size for the brush
DEFAULT_BRUSH_SIZE = 3

# Default opacity for the brush
DEFAULT_BRUSH_OPACITY = 1.0

# Default brush color
DEFAULT_BRUSH_COLOR = QColor(0, 0, 0)

# Default brush shape
DEFAULT_BRUSH_SHAPE = "circle"

#-------------------------------------------------------------------------------
#   Canvas class
#
