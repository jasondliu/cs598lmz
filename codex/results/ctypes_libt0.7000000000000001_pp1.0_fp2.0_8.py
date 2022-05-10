import ctypes
ctypes.windll.user32.MessageBoxW(0, "You have been notified!", "Notification", 0)

# import time
# import sys
# from PyQt5.QtCore import QTimer
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
# from PyQt5.QtGui import QIcon
#
#
# class App(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 simple window - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 480
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         label = QLabel('Python', self)
#         label.move(50,
