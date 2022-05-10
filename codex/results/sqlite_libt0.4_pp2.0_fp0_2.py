import ctypes
import ctypes.util
import threading
import sqlite3
import time
import json
import os
import sys
import re
import datetime
import logging

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GdkPixbuf', '2.0')
gi.require_version('GObject', '2.0')
gi.require_version('GLib', '2.0')
gi.require_version('Gio', '2.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject, GLib, Gio

from . import utils
from . import settings
from .utils import _, ngettext

from . import models
from . import controllers
from . import views
from . import plugins

from . import logger
log = logger.getLogger(__name__)

# TODO:
# * add a "try again" button to the error dialogs
# * add a "clear" button to the search entry
# * add a "clear" button to
