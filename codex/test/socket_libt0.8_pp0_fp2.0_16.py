import socket
import sys
import threading

# from PIL import Image

from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.uic import loadUi
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtSql import QSqlTableModel
from Ftp_connection import ftp_connection
