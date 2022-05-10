import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import os.path
import re
import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from . import config
from . import global_vars
from . import utils
from . import app_utils
from . import download_utils
from . import about_dialog
from . import preferences_dialog
from . import add_torrent_dialog
from . import add_metalink_dialog
from . import create_torrent_dialog
from . import trackers_dialog
from . import add_trackers_dialog
from . import properties_dialog
from . import create_torrent_dialog
from . import session_stats_dialog
from . import torrent_details_dialog
from . import add_peers_dialog
from . import ban_peers_dialog
from . import upload_speed_dialog
