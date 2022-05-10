import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gtk
import gobject

import gettext
_ = gettext.gettext

import os
import sys
import urllib

from sugar.activity import activity
from sugar.graphics.alert import ConfirmationAlert, ErrorAlert
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityToolbarButton
from sugar.activity.widgets import StopButton
from sugar.graphics.toolbutton import ToolButton
from sugar.graphics.toggletoolbutton import ToggleToolButton
from sugar.graphics.menuitem import MenuItem
from sugar.graphics.icon import Icon

import logging
_logger = logging.getLogger('read-activity')

import model
import webkit
import json
import epub
import book
import html
import settings

try:
    import speech
except:
    _logger.debug('speech not available')
