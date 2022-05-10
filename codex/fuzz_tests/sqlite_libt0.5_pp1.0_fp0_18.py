import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import os
import sys
import re
import tempfile
import traceback
import shutil

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gtk, Gdk, GObject

import pkg_resources
import pycountry

from . import lib, utils, constants, config, database
from .constants import *

# Check if we have the new Gtk.FileChooserNative API
try:
    Gtk.FileChooserNative
    native_filechooser = True
except AttributeError:
    native_filechooser = False

# Check if we have the new Gtk.FlowBox API
try:
    Gtk.FlowBox
    flowbox = True
except AttributeError:
    flowbox = False

# Check if we have the new Gtk.SearchBar API
try:
    Gtk.SearchBar
    searchbar = True
except AttributeError:
    searchbar = False

#
