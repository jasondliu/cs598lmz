import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import atexit
import tempfile
import shutil
import re
import subprocess
import time
import random
import string
import errno

import gtk
import gobject

from sugar.activity import activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityToolbarButton
from sugar.activity.widgets import StopButton
from sugar.graphics.toolbutton import ToolButton
from sugar.graphics.menuitem import MenuItem
from sugar.graphics.alert import Alert
from sugar.graphics.objectchooser import ObjectChooser
from sugar.graphics.icon import Icon
from sugar.graphics.xocolor import XoColor

import logging
_logger = logging.getLogger('Model-Viewer-Activity')

class ModelViewerActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        self.model_file = None

