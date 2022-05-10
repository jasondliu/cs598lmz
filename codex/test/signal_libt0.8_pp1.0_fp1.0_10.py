import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import os.path as osp
import sys
import argparse

from PyQt5.QtCore import QSettings

from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication

from labelme.utils.qpixmap2img import QPixmapToImage


# https://github.com/wkentaro/labelme/blob/master/examples/semantic_segmentation/semantic_segmentation.py
# https://stackoverflow.com/questions/10655798/pyqt-how-to-make-a-scrollable-window

