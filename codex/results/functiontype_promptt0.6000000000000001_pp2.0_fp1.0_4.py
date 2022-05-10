import types
# Test types.FunctionType, but not on Python 3, where it's gone.
import sys
if sys.version_info[0] < 3:
    if hasattr(types, 'FunctionType'):
        from types import FunctionType
    else:
        FunctionType = type(lambda: None)

import os
import sys
import time
import unittest
try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

import dbus
import dbus.service

from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstPbutils', '1.0')
from gi.repository import Gst, GstPbutils

import pitivi
from pitivi.configure import get_pixmap_dir, get_ui_dir
from pitivi.project import ProjectManager
from pitivi.timeline.timeline import TimelineContainer
from
