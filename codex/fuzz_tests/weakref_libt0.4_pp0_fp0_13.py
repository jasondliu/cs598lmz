import weakref
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread, QTimer
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
from PyQt5.QtGui import QPixmap, QImage

from . import ui_mainwindow
from . import ui_about
from . import ui_settings
from . import ui_new_project
from . import ui_project_settings
from . import ui_new_image
from . import ui_new_label
from . import ui_label_settings
from . import ui_image_settings
from . import ui_new_detector
from . import ui_detector_settings
from . import ui_new_classifier
from . import ui_classifier_settings
from . import ui_new_segmenter
from . import ui_segmenter_settings
from . import ui
