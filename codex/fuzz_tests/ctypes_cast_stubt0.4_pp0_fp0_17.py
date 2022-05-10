import ctypes
ctypes.cast(0, ctypes.py_object)

# Import the core and GUI elements of Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Import the code for the dialog
from ui_calculator import Ui_Calculator

# Create a class for our main window
class Calculator(QMainWindow, Ui_Calculator):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.setupUi(self)

        self.btn0.clicked.connect(self.btn0_clicked)
        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)
        self.btn3.clicked.connect(self.btn3_clicked)
        self.btn4.clicked.connect(self.btn4_clicked)
        self.btn5.cl
