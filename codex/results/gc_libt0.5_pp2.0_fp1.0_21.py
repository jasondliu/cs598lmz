import gc, weakref

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from . import utils
from .canvas import Canvas
from .settings import SettingsDialog
from .labelDialog import LabelDialog
from .colorDialog import ColorDialog
from .labelFile import LabelFile
from .toolBar import ToolBar
from .pascal_voc_io import PascalVocReader
from .pascal_voc_io import XML_EXT
from .yolo_io import YoloReader
from .yolo_io import TXT_EXT
from .shape import Shape, DEFAULT_LINE_COLOR, DEFAULT_FILL_COLOR

from . import __appname__
from . import __version__

CURSOR_DEFAULT = Qt.ArrowCursor
CURSOR_POINT = Qt.PointingHandCursor
CURSOR_DRAW = Qt.CrossCursor
CURSOR_MOVE = Qt.ClosedHandCursor
CURSOR_GRAB = Qt.
