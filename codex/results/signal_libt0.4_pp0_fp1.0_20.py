import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gtk
import gobject

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityToolbarButton
from sugar.activity.widgets import StopButton
from sugar.graphics.toolbutton import ToolButton
from sugar.graphics.menuitem import MenuItem

from gettext import gettext as _

from sugar import profile

import os
import commands
import subprocess
import logging

from sugar.presence import presenceservice

from sugar.presence.tubeconn import TubeConnection

from dbus.service import signal

from dbus.gobject_service import ExportedGObject

from dbus import Interface, DBusException

from jarabe.model import bundleregistry
from jarabe.model import shell
from jarabe.model import clipboard

from jarabe.journal import misc
from jarabe.journal import model

from jarabe.journal import journalentry

from jarabe.journal import datast
