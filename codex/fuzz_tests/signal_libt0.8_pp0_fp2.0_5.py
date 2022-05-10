import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# The following code is to disable PySide/PyQt window close button
# Right now we use PyQt4 because of performance issues with PySide
# The code is pretty much a copy-paste from https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
# It is licensed under CC BY-SA 3.0 https://creativecommons.org/licenses/by-sa/3.0/
class TaskBarIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QtGui.QMenu(parent)
        exitAction = self.menu.addAction("Exit")
        self.setContextMenu(self.menu)
        self.connect(exitAction, QtCore.SIGNAL('triggered
