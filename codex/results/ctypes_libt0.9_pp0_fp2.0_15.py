import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(2)

from PyQt4 import QtGui
from pyqtgraph.widgets.RawImageWidget import RawImageWidget


class AORawImageWidget(RawImageWidget):
    def __in
