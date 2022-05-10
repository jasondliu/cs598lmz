import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('sp_mep_companion')

from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                             QComboBox, QDialogButtonBox, QVBoxLayout,
                             QPushButton, QRadioButton, QHBoxLayout,
                             QGroupBox, QWidget)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon


class Mep(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MEP Companion')
        self.setWindowIcon(QIcon('mep_gen_1.ico'))
        self.generator_dialog = GeneratorDialog()
        self.layout = QVBoxLayout()
        self.generate_button = QPushButton('Generate MEP')
        self.generate_button.clicked.connect(self.generator_dialog.show)
        self.layout.add
