import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os, sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt, QCoreApplication
from get_timestamp import get_timestamp
from trans import Translator
import re

home_dir = os.path.expanduser('~')

log_path = os.path.join(home_dir, 'log.txt')
with open(log_path, 'a') as f:
    f.write(get_timestamp() + '\n')

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('8-bit Translator')
w.setGeometry(300, 300, 600, 300)
w.setWindowFlags(Qt.CustomizeWindowHint)

layout = QGridLayout()
layout.setHorizontalSpacing(1)
layout.setVerticalSpacing(0)

label1 = QLabel
