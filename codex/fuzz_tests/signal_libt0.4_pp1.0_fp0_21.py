import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap, QImage

from ui_main import Ui_MainWindow
from ui_about import Ui_About
from ui_settings import Ui_Settings
from ui_settings_camera import Ui_Settings_Camera
from ui_settings_image import Ui_Settings_Image
from ui_settings_network import Ui_Settings_Network
from ui_settings_stream import Ui_Settings_Stream
from ui_settings_video import Ui_Settings_Video
from ui_settings_audio import Ui_Settings_Audio
from ui_settings_text import Ui_Settings_Text

from settings_camera import Settings_Camera
from settings_image import Settings_Image
from settings_network import Settings_Network
from settings_stream import Settings
