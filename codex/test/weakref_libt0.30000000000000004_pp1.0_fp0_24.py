import weakref

from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import Pango
from gi.repository import GLib
from gi.repository import GtkSource

from gi.repository import Gedit

from . import utils
from . import settings
from . import preferences
from . import plugin_loader
from . import plugin_manager
from . import plugin_preferences
from . import plugin_preferences_dialog
from . import plugin_preferences_page
from . import plugin_preferences_window
from . import plugin_preferences_window_activatable
from . import plugin_preferences_window_helper
from . import plugin_preferences_window_panel
from . import plugin_preferences_window_panel_activatable
from . import plugin_preferences_window_panel_helper
