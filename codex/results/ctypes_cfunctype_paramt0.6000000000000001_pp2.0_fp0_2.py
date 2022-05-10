import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

import logging
log = logging.getLogger(__name__)

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk, GLib

from pychess.System import conf
from pychess.System.Log import log
from pychess.System.prefix import addDataPrefix
from pychess.System.idle_add import idle_add
from pychess.System.ThreadPool import pool
from pychess.Utils.const import *
from pychess.Utils.lutils.lmovegen import genAllMoves
from pychess.Utils.lutils.lmove import listToMoves
from pychess.Utils.lutils.LBoard import LBoard
from pychess.Utils.lutils.lsearch import search
from pychess.Utils.lutils.lmove import toSAN
from pychess.Utils.lutils.lmove import
