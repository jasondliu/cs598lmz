import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QSizePolicy
from PyQt5.QtGui import QPixmap, QImage, QKeySequence
from PyQt5.QtCore import QDir, Qt, QUrl, QThread, QMutex, QMutexLocker
from PyQt5.QtMultimedia import QMediaContent, QMediaRecorder, QAudioEncoderSettings, QCameraInfo, QVideoEncoderSettings
from numpy import array, uint8
from PyQt5.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout, 
    QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class RecordDialog(QDialog):
    """Create RecordDialog class to extend the functionality of Q
