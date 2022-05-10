import ctypes
import ctypes.util
import threading
import sqlite3
import logging

import gobject
import pygst
pygst.require("0.10")
import gst
import glib
import gtk

from sharp.util.misc import Null
from sharp.tasks.base import Task
from sharp.static import lib
from sharp.util.misc import log_last_exception
from sharp.config.load import config
from sharp.data.files.sql import SQLFile
from sharp.data.types.aliases import subdtype
from sharp.gui.windows.gtk.base import show_window
from sharp.gui.windows.gst import EncoderPipeline
from sharp.gui.windows.gst.threading import thread_watch
from sharp.util.base import str2date
from sharp.util.signal import Connection
from sharp.tasks.signal.annotations import AnnotationsLoaded
from sharp.tasks.signal.replay import ReplayRegion
from sharp.tasks.signal.replay import ReplayFinished
from sharp.tasks.signal.replay import ReplayStarted


log = logging.getLogger(
