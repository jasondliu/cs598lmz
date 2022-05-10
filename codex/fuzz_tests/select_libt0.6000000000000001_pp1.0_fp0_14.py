import select
import sys
import time
import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.ttk
import traceback

from . import config
from . import core
from . import scheduler
from . import utils
from . import wm
from . import x

# TODO:
#   - Button to open/close all windows
#   - Button to maximize all windows
#   - Button to show/hide all windows
#   - Window list:
#       - Window title
#       - Window icon
#       - Window class
#       - Window instance
#       - Window PID
#       - Window geometry
#       - Window state (normal, minimized, maximized, fullscreen)
#       - Window type (utility, normal, dialog, desktop, dock, toolbar, menu,
#         splash, tooltip, notification, dropdown menu, popup menu, tooltip)
#       - Window visible
#       - Window input focus
#       - Window mouse over
#       - Window mouse buttons pressed
#       - Window key presses
#   - Window
