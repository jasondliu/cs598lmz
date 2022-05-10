import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk

from kazam.backend.prefs import *
from kazam.frontend.about import AboutKazam
from kazam.frontend.preferences import Preferences
from kazam.frontend.select_area import SelectArea
from kazam.frontend.select_window import SelectWindow
from kazam.frontend.tray import KazamTrayIcon
from kazam.frontend.tray_menu import KazamTrayMenu
from kazam.frontend.video_preview import VideoPreview
from kazam.frontend.window_overlay import WindowOverlay
from kazam.utils import *
from kazam.backend.av_sync import AVsynchronizer
from kazam.backend.notifications import Notification
from kazam.backend.pulseaudio import PulseAudio
from kazam.backend.pulseaudio import PulseAudioError
from kazam.backend.record import Record
