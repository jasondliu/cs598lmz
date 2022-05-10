import weakref, sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject, QThread

from template.mainwindow import Ui_MainWindow
from template.designer import Ui_Form
from template.widget import Ui_Widget
from template.dialog import Ui_Dialog
from template.qml import QmlWindow

from template.pyqt import clickable_qlistwidget
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QApplication, QMessageBox

import template.utils as mru

from functools import partial
from collections import namedtuple

from template.designer import Ui_Form
from template.mainwindow import Ui_MainWindow
