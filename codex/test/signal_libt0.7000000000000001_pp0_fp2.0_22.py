import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from qgis.core import (QgsApplication, QgsVectorLayer, QgsProject, QgsMapSettings, QgsMapRendererParallelJob, QgsMapLayerRegistry, QgsRenderer, QgsRectangle)
from qgis.PyQt import QtGui, QtCore
from qgis.PyQt.QtCore import QSize, QPoint, Qt
from qgis.PyQt.QtWidgets import QLabel, QSizePolicy, QComboBox, QDialogButtonBox, QDialog, QApplication, QWidget, QPushButton, QTableView, QVBoxLayout, QHBoxLayout, QFrame, QMessageBox
from qgis.PyQt.QtGui import QIcon, QPixmap, QPainter

class Canvas(QWidget):
    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)
        self.initUI()

