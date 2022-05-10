import gc, weakref
from collections import defaultdict

from PyQt4 import QtGui, QtCore
from ginga.misc import log
from ginga import colors
from ginga.qtw.QtHelp import QtGui, QtCore
from ginga.qtw.QtHelp import QFont, QFontMetrics, QColor, QPen, QBrush
from ginga.qtw import QtHelp
from ginga.qtw import QtHelp
from ginga import cmap, imap
from ginga.util import dp
from ginga import trcalc
from ginga.qtw import DrawingMixin

class CanvasObjectBase(object):

    def __init__(self, canvas, tag=None):
        self.canvas = weakref.ref(canvas)
        self.tag = tag
        self.kind = 'unknown'
        self.editing = False
        self.cap = 'ball'
        self.cap_radius = 4
        self.cap_fill = True
        self.fill = False
        self.fillcolor = None
