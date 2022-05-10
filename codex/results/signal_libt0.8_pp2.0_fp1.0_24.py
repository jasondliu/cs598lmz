import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtGui import *
from PyQt4.QtCore import *
 

sc = QApplication(sys.argv)

class Application(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.listWidget = QListWidget(self)
        for i in range(0,10):
            self.listWidget.addItem("item %d" % i)
        self.button = QPushButton("Delete Selcted Items")
        self.layoutVertical = QVBoxLayout()
        self.layoutVertical.addWidget(self.button)
        self.layoutVertical.addWidget(self.listWidget)
        self.setLayout(self.layoutVertical)
        self.button.clicked.connect(self.onButtonClicked)
 
    @pyqtSlot()
    def onButtonClicked(self):
        for item in self.listWidget.selectedItems():
            self.
