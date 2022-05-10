import weakref
from typing import Any, Callable, Optional, Type, Union

from qtpy import QtCore, QtGui, QtWidgets


class LineButton(QtWidgets.QPushButton):
    """
    A button with a line edit on the left.

    Parameters
    ----------
    parent: QWidget
        Parent widget.
    """

    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super().__init__(parent=parent)

        # Setup layout
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        # Line edit
        self._line_edit = QtWidgets.QLineEdit()
        self._line_edit.setReadOnly(True)
        self._line_edit.setFocusPolicy(QtCore.Qt.NoFocus)
        layout.addWidget(self._line_edit)

        # Button
        self._button = QtWidgets.QPushButton()
       
