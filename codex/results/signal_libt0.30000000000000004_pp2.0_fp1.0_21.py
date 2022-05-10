import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gtk
import gobject
import pango

import gtk.glade

import os
import sys
import time
import threading
import traceback

import gettext
_ = gettext.gettext

import gtk.gdk

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityToolbarButton
from sugar.activity.widgets import StopButton
from sugar.graphics.toolbutton import ToolButton
from sugar.graphics.radiotoolbutton import RadioToolButton
from sugar.graphics.icon import Icon
from sugar.graphics.alert import Alert
from sugar.graphics.objectchooser import ObjectChooser
from sugar.graphics.objectchooser import FILTER_TYPE_GENERIC_MIME
from sugar.graphics.objectchooser import FILTER_TYPE_GENERIC_TAG
from sugar.graphics.objectchooser import FILTER_TYPE_GENERIC_TEXT
from sugar.g
