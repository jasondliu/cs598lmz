import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtGui import *
from PyQt4 import QtCore

from ui_qt.preference_widget import Ui_MainPreferencesWidget
#from bzr_plugin import BZR_Preferences

class PreferencesDialog(QDialog):
  """Create a preferences dialog."""
  def __init__(self, parent=None):
    super(PreferencesDialog, self).__init__(parent)
    #setup of tab bar
    self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok |
                                      QDialogButtonBox.Cancel)
    self.buttonBox.accepted.connect(self.accept)
    self.buttonBox.rejected.connect(self.reject)
    self.tabWidget = QTabWidget()
    self.mainWidget = MainPreferencesWidget()
    #bzrWidget = BZR_Preferences()
    #self.tabWidget.addTab(self.mainWidget,self.tr("Main Preferences"))
