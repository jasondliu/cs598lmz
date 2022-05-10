import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os

#
# Constants
#

# The following constants are defined in the libspotify.h header file
# and are used by the spotify.Session class.

# The bitrate of the audio stream.
#
# One of 96k, 160k or 320k.
SP_BITRATE_96k = 0
SP_BITRATE_160k = 1
SP_BITRATE_320k = 2

# The repeat mode of the playback.
#
# One of off, track or context.
SP_REPEAT_OFF = 0
SP_REPEAT_TRACK = 1
SP_REPEAT_CONTEXT = 2

# The shuffle mode of the playback.
#
# One of off or on.
SP_SHUFFLE_OFF = 0
SP_SHUFFLE_ON = 1

# The playback status.
#
# One of undefined, loading, playing, paused or stopped.
SP_PLAYBACK_STATUS_UNDEFINED = 0
SP_PLAYBACK_STATUS_PLAYING = 1
SP_
