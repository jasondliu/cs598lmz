import weakref

from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Gst

from pitivi.configure import get_ui_dir
from pitivi.utils.loggable import Loggable
from pitivi.utils.misc import disconnectAllByFunc
from pitivi.utils.ui import SPACING, PADDING, \
    beautify_length, beautify_time_delta, beautify_stream_name, \
    get_combo_value, set_combo_value
from pitivi.utils.widgets import GstElementSettingsWidget
from pitivi.utils.widgets import PixbufBin
from pitivi.utils.widgets import TimeWidget

# pylint: disable=E1101


# FIXME: This should be in a separate file
class AudioLevels(Gtk.DrawingArea):

    """Widget for displaying audio levels."""

   
