import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
#from PyQt5.Qt import QIcon

from gui.main_window import Ui_MainWindow
from gui.about_window import Ui_AboutWindow
from gui.add_window import Ui_AddWindow
from gui.delete_window import Ui_DeleteWindow
from gui.edit_window import Ui_EditWindow

from gui.add_group_window import Ui_AddGroupWindow
from gui.edit_group_window import Ui_EditGroupWindow
from gui.delete_group_window import Ui_DeleteGroupWindow

from gui.add_repo_window import Ui_AddRepoWindow
from gui.edit_repo_window import Ui_EditRepoWindow
from gui.delete_repo_window import Ui_DeleteRepoWindow

from gui.add_key_window import Ui_AddKeyWindow
from gui.delete_key_window import Ui
