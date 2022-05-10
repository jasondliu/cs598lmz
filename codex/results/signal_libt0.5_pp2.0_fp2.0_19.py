import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# For testing purposes
if __name__ == '__main__':
    import sys
    sys.path.append('../')

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from mainwindow import MainWindow

class MainWindowTest(QApplication):

    def __init__(self):
        super(MainWindowTest, self).__init__(sys.argv)

        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def run(self):
        self.exec_()

if __name__ == '__main__':
    mainWindowTest = MainWindowTest()
    mainWindowTest.run()
