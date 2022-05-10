import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog

from modules.gui.main_window import Ui_Dialog
from modules.gui.settings_dialog import Ui_SettingsDialog
from modules.gui.plot_dialog import Ui_PlotDialog
from modules.gui.about_dialog import Ui_AboutDialog
from modules.gui.keyboard_dialog import Ui_KeyboardDialog
from modules.gui.user_guide_dialog import Ui_UserGuideDialog
from modules.gui.settings_dialog import Ui_SettingsDialog
from modules.gui.message_box import Ui_MessageBox
from modules.gui.confirmation_box import Ui_ConfirmationBox
from modules.gui.input_dialog import Ui_InputDialog

from modules.measurement.measurement import Measurement
from modules.measurement.measurement_worker import MeasurementWorker
from modules.measurement.measure
