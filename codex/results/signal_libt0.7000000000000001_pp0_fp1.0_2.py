import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QString
from mpl_toolkits.basemap import Basemap

from ui_mw import Ui_MainWindow
from ui_dialog_settings import Ui_Dialog_Settings
from ui_dialog_new_proj import Ui_Dialog_NewProj
from ui_dialog_setup_map import Ui_Dialog_SetupMap
from ui_dialog_view_data import Ui_Dialog_ViewData
from ui_dialog_print_report import Ui_Dialog_PrintReport
from ui_dialog_about import Ui_Dialog_About
from ui_dialog_debug import Ui_Dialog_Debug
from ui_dialog_report_options import Ui_Dialog_ReportOptions
from ui_dialog_select_site import Ui_Dialog_SelectSite
from ui_dialog_edit_site import Ui_
