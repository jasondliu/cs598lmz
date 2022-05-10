import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import subprocess
import threading
import re
import tempfile
import shutil

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk, Gdk, GObject, GtkSource, Pango

import editor
import dialog
import utils
import config
import preferences
import project
import plugin
import vcs
import gedit
import log
import dbg
import doc
import run
import search
import sidebar
import completion
import findinfiles
import build
import bookmarks
import gdb
import gobject_worker
import clang_completion
import clang_diagnostics
import clang_format
import clang_rename
import clang_tidy
import clang_include_fixer
import clang_tidy_fix
import clang_
