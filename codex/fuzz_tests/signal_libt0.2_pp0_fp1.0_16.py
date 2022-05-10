import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon

from . import __version__
from . import __appname__
from . import __description__
from . import __author__
from . import __email__
from . import __license__
from . import __copyright__
from . import __url__

from . import __config__
from . import __config_file__

from . import __logo__

from . import __default_config__

from . import __default_config_file__

from . import __default_config_file_name__

from . import __default_config_file_path__

from . import __default_config_file_path_name__

from . import __default_config_file_path_name_ext__

from . import __default_config_file_path_name
