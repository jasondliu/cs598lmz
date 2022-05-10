import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk, GObject, GdkPixbuf, Pango

from kazam.backend.prefs import *
from kazam.backend.utils import *
from kazam.backend.pulseaudio import *
from kazam.frontend.prefs_dialog import *
from kazam.frontend.about_dialog import *
from kazam.frontend.video_preview import *
from kazam.frontend.video_editor import *
from kazam.frontend.video_player import *
from kazam.frontend.trayicon import *
from kazam.frontend.notify import *
from kazam.frontend.notify_osd import *
from kazam.frontend.notify_libnotify import *
from kazam.frontend.notify_gnotification import *
from kazam.frontend.notify_dummy import *
from
