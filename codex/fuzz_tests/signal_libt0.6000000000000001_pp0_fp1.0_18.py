import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# for window close event
from PyQt4.QtCore import QTimer, SIGNAL, SLOT

# for PyQt application
from PyQt4.QtGui import QApplication

# for vtk window
from vtk import vtkGenericRenderWindowInteractor, QVTKRenderWindowInteractor

# for class
from .MainWindow import MainWindow

class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.mainWindow = MainWindow()
        self.mainWindow.show()
        self.connect(self, SIGNAL("lastWindowClosed()"), SLOT("quit()"))

if __name__ == "__main__":
    app = App(sys.argv)
    app.exec_()
