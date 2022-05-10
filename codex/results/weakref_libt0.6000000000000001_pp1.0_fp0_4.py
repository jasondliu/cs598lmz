import weakref

from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
    QPlainTextEdit, QLineEdit, QCheckBox, QComboBox, QProgressBar, QWidget, QSizePolicy, QGroupBox, QMessageBox

from electrum.i18n import _
from electrum.util import format_satoshis, format_fee_satoshis, format_satoshis_plain
from electrum.bitcoin import COIN, is_address
from electrum.plugins import run_hook

from .util import Buttons, HelpLabel, CloseButton, MessageBoxMixin, EnterButton, ColorScheme
from .qrcodewidget import QRCodeWidget, QRDialog
from .qrtextedit import ShowQRTextEdit
from .amountedit import AmountEdit
from .fee_slider import FeeSlider


class EnterButton(QPushButton):
    def __init__(self, text, func):

