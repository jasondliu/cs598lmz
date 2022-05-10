import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import os
import gtk
import gobject
import pango
import time

try:
    import glib
except:
    import gobject as glib

import pynotify
if not pynotify.init('Notification'):
    sys.exit(1)

try:
    import pygame
    from pygame.locals import *
    pygame.mixer.init(44100, -16, 2, 1024)
except:
    print "Couldn't load pygame."
    sys.exit(1)

def get_file_path(filename):
    if getattr(sys, 'frozen', None):
        return os.path.join(os.path.dirname(sys.executable), filename)
    else:
        return os.path.join(os.path.dirname(__file__), filename)

def get_image_path(filename):
    return get_file_path(os.path.join('images', filename))

def
