import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 781, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../../../home/peter/Documents/programming/python/python_qt/qt_tutorial/images/qt_logo.png"))
        self.label.setObjectName("label")
