import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.Qt import QTextDocument
from PyQt4.QtGui import QTextDocumentWriter

from ui.ui_main import Ui_MainWindow
from ui.ui_find import Ui_FindDialog
from ui.ui_replace import Ui_ReplaceDialog
from ui.ui_new import Ui_NewDialog
from ui.ui_about import Ui_AboutDialog
from ui.ui_settings import Ui_SettingsDialog
from ui.ui_options import Ui_OptionsDialog
from ui.ui_options_editor import Ui_OptionsEditorDialog
from ui.ui_options_fonts import Ui_OptionsFontsDialog
from ui.ui_options_shortcuts import Ui_OptionsShortcutsDialog
from ui.ui_options_preview import Ui_OptionsPreviewDialog
