import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
from ui import Ui_MainWindow
from tp import Tp
import os
import time

# 窗体类
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.comboBox.addItems(['压力','湿度','温度'])

        # 定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_graph)
        self.timer.start(1000)

        self.tp = Tp()

    def refresh_graph(self):
        b
