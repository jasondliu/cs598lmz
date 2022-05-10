import socket
import sys
import json
import struct
import time
import threading

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QHBoxLayout, QVBoxLayout, QLineEdit, \
    QPushButton, QLabel, QMessageBox, QTreeWidgetItemIterator, QDoubleSpinBox, QSpinBox, QAbstractItemView
from PyQt5.QtGui import QIcon

# global variable
# 数据库存储的数据
global_list = []
# 当前选中的设备
global_cur_device = None
# 记录当前的选中的设备
global_cur_device_num = -1
# 记录当前的选中的项目
global_cur_project_num = -1
#
