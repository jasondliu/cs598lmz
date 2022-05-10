import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
from sqlite3 import dbapi2 as sqlite
import os
from contextlib import closing
from zipfile import ZipFile
import json
import sys
import time

# Global variables

# The number of the current song playing
current_song = 0
# The current song's information
song_data = []
# The current song's file
song_file = ''
# The current album's directory
album_dir = ''

# The main window
main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
# The main window's vertical container
vbox = gtk.VBox()
# The main window's horizontal container
hbox = gtk.HBox()

# The album cover image
image = gtk.Image()
# The current song's information
label = gtk.Label()
# The current time
time_label = gtk.Label()

# The progress bar
progress = gtk.ProgressBar()

# The play/pause button
play_button = gtk.Button()
play_image = gtk.Image()
play_image.set_
