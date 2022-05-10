import mmap
import os
import re
import sys
import tempfile
import time
import webbrowser

from . import log
from . import util
from . import vcs
from . import version
from . import xdg
from . import xdg_cache
from . import xdg_config
from . import xdg_data
from . import xdg_data_home
from . import xdg_data_dirs
from . import xdg_data_dirs_no_prefix
from . import xdg_data_dirs_prefix
from . import xdg_data_home_no_prefix
from . import xdg_data_home_prefix
from . import xdg_data_no_prefix
from . import xdg_data_prefix
from . import xdg_desktop_entry_validate
from . import xdg_desktop_menu_validate
from . import xdg_icon_resource
from . import xdg_icon_theme
from . import xdg_icon_theme_list
from . import xdg_icon_theme
