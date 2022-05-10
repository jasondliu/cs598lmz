import mmap
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
import tkinter as tk
import traceback
from collections import OrderedDict
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

from PIL import Image, ImageTk
from core.utils import *
from core.utils import _

from . import preferences, welcome, update
from .about import About
from .config import Config
from .startup import Startup
from .utils import *

from core.backend.lib.helpers import *


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Create tk instance, set window title, and set window icon
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Cura LulzBot Edition')
        self.iconbitmap(get_icon_location('c
