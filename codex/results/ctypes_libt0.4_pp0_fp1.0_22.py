import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QIcon

from qml.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/assets/icons/icon.png"))

    engine = QQmlApplicationEngine()
    engine.load(QUrl("qml/main.qml"))

    mainwindow = MainWindow()
    mainwindow.show()

    sys.exit(app.exec_())
