import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from about_dialog import AboutDialog
from main_dialog import MainDialog
from main_dialog_ui import Ui_MainDialog
import os.path


class MainWindow(QMainWindow, Ui_MainDialog):
    def __init__(self, parent=None):
        """Constructor."""
        super(MainWindow, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def about(self):
        dlg = AboutDialog()
        dlg.exec
