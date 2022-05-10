import weakref

# PyQt5 Imports
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QTreeWidgetItem, QPushButton

# Own Imports
from kmap import __directory__
from kmap.library.misc import get_icon
from kmap.library.plotting.plot1d import Plot1D
from kmap.library.plotting.plot2d import Plot2D
from kmap.library.plotting.plot3d import Plot3D


class PlotTree(QTreeWidgetItem):

    def __init__(self, name, parent=None, plot=None, parent_class=None,
                 icon=None, checkable=False, expand=False):

        QTreeWidgetItem.__init__(self, parent)

        self.name = name
        self.expanded = expand
        self.checkable = checkable

        self.__parent_class = parent_class

