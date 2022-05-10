import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

from . import __version__
from . import __author__
from . import __email__
from . import __url__
from . import __license__
from . import __copyright__
from . import __description__

from . import config
from . import resources
from . import utils
from . import widgets
from . import models
from . import views
from . import controllers

from . import settings
from . import mainwindow
from . import aboutdialog
from . import preferencedialog
from . import newprojectdialog
from . import newprojectwizard
from . import newprojectwizardpage1
from . import newprojectwizardpage2
from . import newprojectwizardpage3
from . import newprojectwizardpage4
from . import newprojectwizardpage5
from . import newprojectwizardpage6
