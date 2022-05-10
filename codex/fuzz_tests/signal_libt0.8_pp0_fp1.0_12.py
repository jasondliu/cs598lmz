import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from gi.repository import Gtk, Gdk, GdkX11
from gi.repository import GObject

import sys
import os
import time
from datetime import datetime
from subprocess import Popen, PIPE, DEVNULL
from threading import Thread
from math import floor

from gi.repository import Gst
from os import path

from src.utils.utils import get_absolute_path
from src.utils.file_utils import get_home_dir, get_git_ignored_dirs, get_video_thumbnail, get_video_duration
from src.utils.config_utils import get_config
from src.utils.log_utils import create_logger

from src.preview_window.preview_window import PreviewWindow
from src.command_runner.command_runner import CommandRunner
from src.overlay_generator.overlay_generator import OverlayGenerator
from src.cut_window.cut_window import CutWindow
from
