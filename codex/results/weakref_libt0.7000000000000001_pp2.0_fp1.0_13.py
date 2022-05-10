import weakref

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon, QColor, QPainter, QBrush, QPen, QPalette
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QScrollArea, QPushButton, QFrame, QSplitter

from FileType import FileType
from Task import Task
from TaskPool import TaskPool
from TaskWidget import TaskWidget
from constants import *
from create_task_panel import CreateTaskPanel


class TaskPoolWidget(QWidget):

    """
    TaskPoolWidget是一个Widget容器，用来存放TaskWidget
    """

    def __init__(self, task_pool, parent=None):
        super(TaskPoolWidget, self).__init__(parent)
        self.setFixedWidth(TASK_POOL_WIDGET_W
