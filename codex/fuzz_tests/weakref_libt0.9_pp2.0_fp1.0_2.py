import weakref

import builder
import elements
import toolpool
import widgets
import plotting

class MdiWindow(QtWidgets.QMdiArea):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow

        self.roadSet = []
        self.elementSet = []
        self.closeChildSignal = pyqtSignal(widgets.MdiChild)

        self.subWindowListSignal = pyqtSignal(QtWidgets.QMdiSubWindow)
        self.subWindowActivatedSignal = pyqtSignal(QtWidgets.QMdiSubWindow)

    def newChild(self):
        child = widgets.MdiChild(self.mainwindow)
        self.addSubWindow(child)

        # Add tab order
        self.setTabOrder(self.previousChild(child), child.namebox)
        self.setTabOrder(child.namebox, child.toolbox)
        self.setTabOrder(child.toolbox, child.elementbox)
        self
