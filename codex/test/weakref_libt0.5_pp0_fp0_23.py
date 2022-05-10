import weakref

from PyQt5.QtCore import Qt, QModelIndex, QVariant
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QTableView, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit

from tribler_core.modules.libtorrent.download_config import DownloadConfigInterface
from tribler_core.utilities.unicode import hexlify

from tribler_gui.defs import BUTTON_TYPE_NORMAL
from tribler_gui.dialogs.dialogcontainer import DialogContainer
from tribler_gui.utilities import format_size, get_image_path, get_gui_setting
from tribler_gui.widgets.custom_toolbutton import CustomToolButton


class DownloadInfoDialog(DialogContainer):
    """
    This dialog shows information about a specific download.
    """

    def __init__(self, parent, download):
        DialogContainer.__init__(self, parent)
        self.download = download

