import weakref
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                             QSplitter, QAction, QPushButton, QMenu,
                             QFileDialog)
from PyQt5.QtSql import (QSqlQueryModel, QSqlTableModel)

from .views import (FileList, ResultList)
from .languages import get_language_by_filename, get_files_for_lang
from .tabs import SearchTabWidget
from .workers import (ScanWorker, SearchWorker, IndexWorker,)
from .dialogs import (FileDialog, DirectoryDialog,
                      SearchDialog, PreferencesDialog,
                      MessageDialog)
from .app import settings
from . import __appname__, __version__
from . import logger
from . import __prog__
from .tr import tr as _


class MainWindow(QWidget):

    def __init__(self, parent=None):

