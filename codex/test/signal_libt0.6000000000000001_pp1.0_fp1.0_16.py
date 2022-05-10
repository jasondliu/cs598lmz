import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QPushButton,
    QCheckBox,
    QLineEdit,
    QLabel,
    QComboBox,
    QFileDialog,
    QMessageBox,
    QProgressBar,
    QMenu,
    QAction,
    QSizePolicy,
    QScrollArea,
    QGridLayout,
    QSplitter,
    QStatusBar,
    QTabWidget,
    QDialog,
    QDialogButtonBox,
    QAbstractItemView,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QSystemTrayIcon,
    QStyle,
    QDesktopWidget,
    QFontDialog,
)
from PyQt5.QtCore import Qt, QTimer, QCoreApplication, QSize, QThread

