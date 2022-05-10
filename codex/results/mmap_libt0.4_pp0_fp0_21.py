import mmap
import os
import sys
import time
import traceback
from threading import Thread

from ctypes import *
from ctypes.wintypes import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui import *

from ui.ui_settings import Ui_Settings
from ui.ui_about import Ui_About
from ui.ui_log import Ui_Log

from ui.ui_settings import Ui_Settings
from ui.ui_about import Ui_About
from ui.ui_log import Ui_Log

from ui.ui_edit_profile import Ui_EditProfile
from ui.ui_edit_profile_mode import Ui_EditProfileMode
from ui.ui_edit_profile_mode_advanced import Ui_EditProfileModeAdvanced
from ui.ui_edit_profile_mode_custom import Ui_EditProfileModeCustom
from ui.ui_edit_profile_
