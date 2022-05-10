import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import (Qt, QUrl, QTimer, QEvent, QPoint, QSize, QMargins,
                          QPointF, QRectF, QLineF, QLine, QThread, pyqtSignal,
                          pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QFont, QFontMetrics, QIcon, QImage,
                         QPainter, QPen, QPixmap, QPolygonF, QTransform,
                         QKeySequence)
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QFileDialog,
                             QFrame, QGraphicsView, QGraphicsScene, QLabel,
                             QMainWindow, QMenu, QMessageBox, QSizePolicy,
                             QSplitter, QStatusBar, QToolBar, QVBoxLayout,
                             QWidget, QShortcut, QInputDialog, QLineEdit)
from PyQt
