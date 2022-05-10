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
from . import __long_description__

from . import __app_name__
from . import __app_display_name__

from . import __organization_name__
from . import __organization_domain__

from . import __desktop_file_name__
from . import __desktop_file_path__
from . import __desktop_file_categories__
from . import __desktop_file_mime_types__
from . import __desktop_file_exec_command__

from . import __app_icon__
from . import __app_icon_path__

from . import __app_splash_screen__
from . import __app_splash
