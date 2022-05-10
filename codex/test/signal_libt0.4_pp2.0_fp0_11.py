import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

from .ui.main_window import Ui_MainWindow
from .ui.preferences_dialog import Ui_PreferencesDialog
from .ui.about_dialog import Ui_AboutDialog
from .ui.file_dialog import Ui_FileDialog
from .ui.image_viewer import Ui_ImageViewer
from .ui.image_viewer_dialog import Ui_ImageViewerDialog
from .ui.image_viewer_dialog_fullscreen import Ui_ImageViewerDialogFullscreen
from .ui.image_viewer_dialog_fullscreen_x11 import Ui_ImageViewerDialogFullscreenX11
from .ui.image_viewer_dialog_fullscreen_qt import Ui_ImageViewerDialogFullscreenQt
