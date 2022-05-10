import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

f = open(os.path.expanduser("~/Desktop/python_log.txt"),"w+")
f.write("I am a log file\n")
f.close()

from PyQt4.QtGui import *
from PyQt4.QtCore import *
class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("My first window")
        
        self.show()
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
    def keyPressEvent
