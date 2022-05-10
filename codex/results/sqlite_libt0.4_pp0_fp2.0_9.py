import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import re
import struct

import gtk
import gobject

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityToolbarButton
from sugar.activity.widgets import StopButton
from sugar.graphics.toolbutton import ToolButton
from sugar.graphics.alert import NotifyAlert

import logging
_logger = logging.getLogger('pippy-activity')

import pippy
import pippy.moduledb
import pippy.sound

import pippy_activity

try:
    import pygtk
    pygtk.require('2.0')
except:
    pass

try:
    import gtksourceview2
    import gtksourceview2.language
    import gtksourceview2.languagesmanager
    import gtksourceview2.style
    import gtksourceview2.stylescheme
    import gtksourceview2.styleschememanager
except:
    pass

import gettext

