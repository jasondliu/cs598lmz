import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject

from datetime import datetime, timedelta

from collections import deque

from os.path import expanduser
from os import makedirs
from os import path

from crontab import CronTab

import threading
import subprocess

import sys
import os

from pkg_resources import resource_filename

from rq import Queue
from rq.job import Job
from redis import Redis

from .version import version_number

from . import util
from .util import get_setting, save_setting, save_setting_json, load_setting_json
from .util import get_setting_as_bool, save_setting_as_bool
from .util import get_setting_as_float, save_setting_as_float
from .util import get_setting_as_int, save_setting_as_int

from . import
