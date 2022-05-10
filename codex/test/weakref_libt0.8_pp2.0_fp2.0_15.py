import weakref
from PyQt4 import QtCore, QtGui
from ..model.core import *
import Queue

class ViewModel(QtCore.QObject):

    NODE_TYPE = 0
    LINK_TYPE = 1

    child_deleted = QtCore.pyqtSignal(object)

    def __init__(self, world, parent=None):
        super(ViewModel, self).__init__(parent)
        self.world = world
        self.mapping = {}

        self._root = world
        self._root.children_added.connect(self.children_added)
        self._root.children_removed.connect(self.children_removed)
        self._root.children_updated.connect(self.children_updated)
        self._root.data_added.connect(self.data_added)
        self._root.data_removed.connect(self.data_removed)
