import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('db.sqlite3', check_same_thread=False)

# TODO:
#   - add a way to get the current state of the library (e.g. is it playing,
#     is it paused, etc.)
#   - add a way to get the current position in the track
#   - add a way to get the current volume
#   - add a way to get the current repeat mode
#   - add a way to get the current shuffle mode
#   - add a way to get the current track
#   - add a way to get the track list
#   - add a way to get the current playlist
#   - add a way to get the playlist list
#   - add a way to get the current queue
#   - add a way to get the current track metadata
#   - add a way to get the current track cover
#   - add a way to get the current track lyrics
#   - add a way to get the current track rating
#   - add a way to get the current track playback statistics
#   - add a way to get the current track last played date
#   - add a way
