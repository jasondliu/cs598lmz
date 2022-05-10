import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('My Browser')
        self.setGeometry(0,0,800,600)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.python.org'))
        self.setCentralWidget(self.browser)
        self.show()


app = QApplication(sys.argv)
window = MainWindow()
