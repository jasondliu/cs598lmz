import weakref
from functools import partial

from PyQt5.QtCore import Qt, QPoint, QSize, QTimer, QEventLoop
from PyQt5.QtGui import QColor, QFont, QPalette, QKeySequence, QTextCursor
from PyQt5.QtWidgets import (
    QApplication,
    QStyle,
    QWidget,
    QTableView,
    QAbstractItemView,
    QHeaderView,
    QMenu,
    QAction,
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QCheckBox,
    QSpinBox,
    QDoubleSpinBox,
    QSizePolicy,
    QMessageBox,
    QFileDialog,
    QProgressDialog,
)

from Orange.data import Table, Domain, StringVariable, DiscreteVariable, ContinuousVariable
from Orange.widgets import widget, gui, settings
from Orange.wid
