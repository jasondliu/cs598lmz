import weakref

from gi.repository import Gtk, Gdk, GObject

from ...core import config, Input
from ...core.inputhook import InputHookContext
from ...core.interactiveshell import InteractiveShell
from ...core.displayhook import DisplayHook
from ...core.display_pub import DisplayPublisher
from ...core.comms import CommManager
from ...core.history import HistoryManager
from ...core.magics import MagicsManager
from ...core.alias import AliasManager
from ...core.payload import PayloadManager
from ...core.usage import log_usage, log_kernel_info
from ...utils.ipython_display import IpythonDisplay
from ...utils.log import log_output
from ...utils.py3compat import PY3
from ...utils.process import find_cmd, kill_process
from ...utils.signals import Signal
from ...utils.path import filefind
from ...utils.sysinfo import sys_info
from ...utils.io import capture_output
from ...utils.warn import warn, error
from ...utils.terminal import (
    get_termin
