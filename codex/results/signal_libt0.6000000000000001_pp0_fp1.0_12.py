import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

from ui.mainwindow import Ui_MainWindow
from ui.about import Ui_About
from ui.dialog import Ui_Dialog
from ui.progress import Ui_Progress
from ui.settings import Ui_Settings
from ui.tray import Ui_Tray
from ui.welcome import Ui_Welcome
from ui.wizard import Ui_Wizard
from ui.wizard_page_1 import Ui_WizardPage1
from ui.wizard_page_2 import Ui_WizardPage2
from ui.wizard_page_3 import Ui_WizardPage3
from ui.wizard_page_4 import Ui_WizardPage4
from ui.wizard_page_5 import Ui_W
