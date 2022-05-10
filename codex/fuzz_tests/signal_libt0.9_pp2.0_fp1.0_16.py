import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import os
import subprocess
import math
import re

from PyQt5.QtWidgets import QApplication, QColorDialog, QDialog, QFileDialog, QInputDialog, QLineEdit, QListWidgetItem, QMenu, QMessageBox, QWidget, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView
from PyQt5.QtWidgets import QTableView, QTabWidget
from PyQt5.QtWidgets import QLabel, QTextEdit, QSizePolicy
from PyQt5.QtWidgets import QDoubleSpinBox, QCheckBox
from PyQt5.QLabel import QLabel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap, QImage, QPainter, QColor

from PyQt5
