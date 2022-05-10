import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf

from sugar3.activity import activity
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import ActivityToolbox
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.activity.widgets import ShareButton

from sugar3.graphics.alert import Alert
from sugar3.graphics.alert import NotifyAlert

from sugar3.datastore import datastore

import sugargame.canvas
import pygame

import gamelib

class
