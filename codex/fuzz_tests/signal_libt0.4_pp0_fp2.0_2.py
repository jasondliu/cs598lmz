import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QIcon, QPixmap, QLabel, QMovie, QPainter, QBrush, QPen, QColor, QMessageBox, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog, QFileDialog, QSizePolicy, QComboBox, QCheckBox, QGroupBox, QFont, QListWidget, QListWidgetItem, QTabWidget, QFrame, QTableWidget, QTableWidgetItem, QToolBar, QAction, QMenu, QStatusBar, QDialog, QProgressBar, QDialogButtonBox, QGridLayout, QTextEdit, QStyle, QShortcut, QKeySequence
from PyQt4.QtCore import QThread, QTimer, QObject, pyqtSignal, QSize, Qt, QPoint, QUrl, QString, QFile, QIODevice, QTextStream,
