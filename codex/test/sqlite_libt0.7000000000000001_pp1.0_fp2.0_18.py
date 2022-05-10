import ctypes
import ctypes.util
import threading
import sqlite3

# PyPlex
from plex import *
from plex.objects.core.base import Property
from plex.objects.video import *

# Plex Media Server
from PMS import *
from PMS.VideoFiles import VideoFiles
from PMS.Objects import ObjectContainer, DirectoryObject, VideoClipObject, MediaObject

# pysqlite
sqlite3.enable_callback_tracebacks(True)

# Global vars
ART = 'art-default.jpg'
ICON = 'icon-default.png'

# Prefs
PREF_SHOW_ALL = 'ShowAll'
PREF_SHOW_UNWATCHED = 'ShowUnwatched'

# Init the Plex Framework
core = Plex()

# Declare the main container
@handler('/video/plexwatch', TITLE, thumb=ICON, art=ART)
def MainMenu():
    oc = ObjectContainer(title2=TITLE)

    # Get the active sessions
    sessions = GetSessions()

    # Add a "Show All" option
