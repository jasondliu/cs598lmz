import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import sys
import os
import time
import threading
import webbrowser

import config
import file_manager
import tree_view
import main_window
import sidebar
import headerbar
import statusbar
import finder
import tab_bar
import message_dialog
import other_application
import edit_bookmark
import edit_other_application
import edit_shortcut
import edit_file_extension
import edit_mime_type
import edit_name
import edit_open_with
import edit_keyboard_shortcut
import edit_command
import edit_color
import edit_font
import edit_style
import edit_terminal
import edit_terminal_color
import edit_terminal_font
import edit_terminal_style
import edit_terminal_shortcut
import edit_terminal_command
import edit_terminal_name
import edit
