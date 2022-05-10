import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QGridLayout, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QComboBox, QTextEdit, QFrame, QSizeGrip, QCheckBox, QDialogButtonBox
from PyQt5.QtGui import QIcon, QPixmap, QFont, QPalette, QColor, QBrush, QPainter, QPen, QPolygon, QImage, QPicture, QTextCursor, QTextDocument
from PyQt5.QtCore import QSize, Qt, QPoint, QTimer, QDateTime, QDate, QTime, QTextStream, QFile, QIODevice, QTextCodec, QByteArray, QDataStream, QBuffer, QDir
