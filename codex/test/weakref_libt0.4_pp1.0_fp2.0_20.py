import weakref

from PyQt5.QtCore import Qt, QTimer, QObject
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox

from . import config
from . import utils
from . import ui
from . import log
from . import resources
from . import events
from . import settings
from . import widgets

from .widgets import QClickableLabel

from .widgets.QClickableLabel import QClickableLabel
from .widgets.QClickableLabel import QClickableLabel

from .ui.about_ui import Ui_AboutDialog
from .ui.settings_ui import Ui_SettingsDialog
from .ui.updater_ui import Ui_UpdaterDialog
from .ui.add_ui import Ui_AddDialog
from .ui.edit_ui import Ui_EditDialog
from .ui.edit_ui import Ui_EditDialog

from . import updater
from . import add
from . import edit
from . import about
