import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from ui import Ui_MainWindow

from word_parser import WordParser
from word_tree import WordTree

from class_model import ClassModel
from class_item_delegate import ClassItemDelegate

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_word.textChanged.connect(self.on_word_change)
        self.ui.comboBox_class.currentIndexChanged.connect(self.on_class_change)
        self.ui.pushButton_add.clicked.connect(self.add_word)
        self.ui.push
