import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QTimer

from ui.mainwindow import Ui_MainWindow

from ui.about import Ui_AboutDialog
from ui.preferences import Ui_PreferencesDialog

from ui.new_project import Ui_NewProjectDialog
from ui.new_project_wizard import Ui_NewProjectWizard
from ui.new_project_wizard_page1 import Ui_NewProjectWizardPage1
from ui.new_project_wizard_page2 import Ui_NewProjectWizardPage2
from ui.new_project_wizard_page3 import Ui_NewProjectWizardPage3
from ui.new_project_wizard_page4 import Ui_NewProjectWizardPage4
from ui.new_project_wizard_page5 import Ui_NewProjectWizardPage5
