import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gtk

# Set the name of the application.  This is the name that will show up in
# the window title bar, in the application switcher popup, etc.
gtk.window_set_default_icon_name("orte-gui-ee")

from main import MainWindow
from orte.utils.logger import Log, create_file_handler, create_console_handler, create_windows_event_log_handler, create_syslog_handler

from optparse import OptionParser

from orte.utils import get_platform

import sys, os

from orte.utils.launcher import (OS_WINDOWS, OS_LINUX, OS_MACOSX,
                                 create_upload_package, kill_orte_processes,
  
