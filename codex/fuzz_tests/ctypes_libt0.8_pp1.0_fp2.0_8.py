import ctypes
ctypes.windll.user32.SetProcessDPIAware() 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from AutoScrollBar import AutoScrollBar

# MainWindow is where you create the whole window
class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		self.windowTitleChanged.connect(lambda x: self.__update_title())
		self.window().setStyleSheet("""
			background-color: #333;
			""")
		#self.window().setStyle(QStyleFactory.create("Fusion"))
		self.setWindowTitle("My Application")

		layout = QVBoxLayout()

		self.label = QLabel("TEST")
		self.label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
		
