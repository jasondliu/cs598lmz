import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtNetwork import *

from . import settings
from . import utils
from . import dlg_settings
from . import dlg_about
from . import dlg_download
from . import dlg_login
from . import dlg_add_to_playlist
from . import dlg_create_playlist
from . import dlg_delete_playlist
from . import dlg_rename_playlist
from . import dlg_add_bookmark
