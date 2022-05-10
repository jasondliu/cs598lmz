import codecs
codecs.register(lambda name: name == "cp65001" and codecs.lookup("utf_8") or None)
from datetime import datetime
from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File
import pytz

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from subtitles import Subtitles

from tmdb_client import TmdbClient
from gettext import gettext, ngettext
from gi.repository import RB

# try:
#     import gtk_extra
# except ImportError:
#     from sugar3.graphics.gtk_extra import *

try:
    import json
except ImportError:
    # old Python versions
    import simplejson as json

__all__ = ['SubtitlesDB']

SERVICE_URL = "http://api.thesubdb.com"
UPLOAD_SERVICE_URL = "http://sandbox.thesubdb.com
