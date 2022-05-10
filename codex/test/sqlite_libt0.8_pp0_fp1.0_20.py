import ctypes
import ctypes.util
import threading
import sqlite3
import time
import urllib
import re
import os
import tempfile
import shutil

try:
    import pynotify
    pynotify.init(__file__)
except:
    pass

import gtk
import gobject

try:
    import gnomekeyring as gkey
except:
    gkey = None

import gdata.youtube.service
import gdata.service

import console

import socket
try:
    if socket.gethostbyname('www.google.com') is not None:
        pass
    else:
        raise socket.gaierror
except socket.gaierror:
    console.alert('No internet connection.',
                  'You are not connected to the internet. Please connect and try again.')
    raise SystemExit

try:
    import pygame
    pygame.init()
    pygame.mixer.init()
except:
    pass

import pygtk
gtk.gdk.threads_init()

import ConfigParser
config = ConfigParser.ConfigParser()
