import weakref

from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter, QPainterPath, QColor, QPen
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy

from .base import BaseWidget
from .button import Button
from .label import Label


class Dialog(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)

        self.setObjectName("dialog")
        self.setStyleSheet(
            """
            QWidget#dialog {
                background-color: #ffffff;
                border: 1px solid #000000;
                border-radius: 4px;
            }
            """
        )

        self._title_bar = TitleBar(self)
        self._title_bar.setObjectName("title_bar")
        self._title_bar.setStyleSheet
