import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#-------------------------------------------------------------------------------

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import anaconda_logging
log = anaconda_logging.getModuleLogger(__name__)

from pyanaconda.ui.communication import hubQ
from pyanaconda.ui.gui import GUIObject
from pyanaconda.ui.common import FirstbootSpokeMixIn
from pyanaconda.modules.common.constants.services import TIMEZONE
import pyanaconda.localization as localization
from pyanaconda.modules.common.constants.objects import LOCALIZATION
from pyanaconda.modules.common.structures.localization import Language, Keyboard
from pyanaconda.modules.common.structures.clock import TimezoneInfo

from pyanaconda.ui.gui.spokes import NormalSpoke
from pyanaconda.ui.gui.categories.localization import LocalizationCategory

