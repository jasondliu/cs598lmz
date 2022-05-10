import ctypes
import ctypes.util
import threading
import sqlite3
import os
from datetime import datetime, timedelta
from time import sleep
from pathlib import Path
from shutil import get_terminal_size
from string import ascii_lowercase, ascii_uppercase
from clint.textui.progress import Bar as ProgressBar
from clint.textui import puts, colored, indent
from pyfiglet import Figlet
from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence
from pydub.utils import mediainfo

# set up some constants
TERMINAL_SIZE = get_terminal_size()
LOGO = Figlet(font="slant").renderText("SOMA")
HOME_DIR = str(Path.home())
DB_FILE = os.path.join(HOME_DIR, ".soma.db")
DB_SCHEMA = os.path.join(os.path.dirname(os.path.realpath(__file__)), "schema.sql")

# set up some global variables
global_lock =
