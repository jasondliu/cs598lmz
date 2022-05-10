import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import os.path
import tempfile
import random
import string
import shutil
import atexit

import gobject
import gtk
import gtk.gdk
import pango

import libxml2

import gconf

from sugar.activity import activityfactory
from sugar.activity.activityhandle import ActivityHandle
from sugar.activity.activityinfo import get_bundle_path
from sugar.activity.activityinfo import get_bundle_name
from sugar.activity.activityinfo import get_bundle_id
from sugar.activity.activityinfo import get_bundle_version
from sugar.activity.activityinfo import get_activity_root
from sugar.activity.activityinfo import get_icon_file_name
from sugar.activity.activityinfo import get_bundle_instance_path
from sugar.activity.activityinfo import get_activity_path
from sugar.activity.activityinfo import get_bundle_instance_path
from sugar.activity.activityinfo import get_activity_root


