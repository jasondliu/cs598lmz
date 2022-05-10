import socket

# import the main window object (mw) from ankiqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
# import the dialog
from aqt.addcards import AddCards
from anki.hooks import addHook
from anki.utils import stripHTML
from anki.sound import playFromText, clearAudioQueue
from anki.hooks import wrap

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

from threading import Thread

from time import time

import hashlib

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def myFunction():
    # get the number of cards in the current collection, which is stored in
    # the main window
    cardCount = mw.col.cardCount()
