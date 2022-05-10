import codecs
codecs.register_error("strict", codecs.ignore_errors)

from PyQt4 import QtCore, QtGui, QtSvg
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSvg import *
from PyQt4.QtOpenGL import *
from math import *

from nodebox.util.vector import Point
from nodebox.graphics import Canvas, Context
from nodebox.graphics import *

from base import BaseView, get_font_metrics, get_icon
from utils import read_svg, read_svg_string,get_render_manager, get_font_manager, get_engine, clamp
from constants import *
from signals import *

from frame import Frame
from utils import StackedCall
from utils import AWAIT_DELAY

from behaviors.panning import PanningBehavior
from behaviors.selecting import SelectingBehavior, Selector
from behaviors.dragging import DraggingBehavior
from behaviors.scaling import ScalingBehavior
from behaviors
