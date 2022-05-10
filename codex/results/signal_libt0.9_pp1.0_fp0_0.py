import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import matplotlib
matplotlib.rcParams['toolbar'] = 'None'
matplotlib.use('Agg')
from matplotlib import pylab as plt
# plt.ion()

import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../server/app'))
if not path in sys.path:
  sys.path.insert(1, path)
del path

import star_tracker

main_window = QMainWindow()
main_window.setWindowTitle('Star Tracker')

main_widget = QWidget()
main_layout = QVBoxLayout()
main_widget.setLayout(main_layout)
main_window.setCentralWidget(main_widget)

left_widget = QWidget()
left_layout = QVBoxLayout()
left_widget.setLayout(left_layout)

right_widget = QWidget()
right_layout = QV
