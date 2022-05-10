import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import Qt, QSize, QTimer, QPoint, QPointF, QLineF, QRectF, QUrl
from PyQt5.QtGui import QColor, QPixmap, QImage, QPainter, QPen, QBrush, QFont, QIcon, QKeySequence, QPalette, QMovie, QTransform
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QCheckBox, QSpinBox, QMessageBox, QFileDialog, QMainWindow, QMenu, QAction, QStatusBar, QProgressBar, QShortcut, QInputDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtMultimedia import QSound
from PyQt5.QtMultimediaWidgets import QVideoWidget
