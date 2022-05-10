import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import argparse
import random
from uuid import uuid4
import http.cookiejar as cookielib
import shutil
from time import sleep

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineCore import *

from utilfunctions_mods import (
    read_session_cookies_from_firefox,
    move_rom,
    add_extra_columns,
)
from settings import (
    config,
    simple_format_variables,
    settings_window,
)
from settings_window_mods import (
    setup_update_setting_widgets,
    update_setting_widgets,
    update_setting_variables,
)
from match_details_mods import get_match_details
from setup_mods import setup, check_for_new_version
from
