import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTabWidget, QTextEdit, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem, QComboBox, QCheckBox, QProgressBar, QAction, QMenu, QSystemTrayIcon, QStyle, QDialog, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap, QFont, QPalette, QColor
from PyQt5.QtCore import Qt, QThread, QObject, pyqtSignal, QSize, QTimer, QDateTime

import os, sys, time, datetime, json, re, random, string, subprocess, threading, shutil, webbrowser, requests, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse,
