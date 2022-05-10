import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, GObject

from lutris import pga
from lutris.config import LutrisConfig
from lutris.gui import icons
from lutris.gui.dialogs import QuestionDialog, UpdateDialog, ImportDialog, \
    LutrisDialog, AddGameDialog, ConfigurationDialog, PreferencesDialog
from lutris.gui.gamestore import GameStore
from lutris.gui.installedwidget import InstalledGamesWidget
from lutris.gui.runnerconfig import RunnerConfigDialog
from lutris.gui.widgets.search import SearchEntry
from lutris.gui.widgets.utils import GtkBuilderTemplate
from lutris.persistence import db
from lutris.thread import LutrisThread
from lutris.util import system


logger = logging.getLogger(__name__)


