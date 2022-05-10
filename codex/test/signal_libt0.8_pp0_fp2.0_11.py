import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GtkSource", "3.0")
from gi.repository import Gtk, GtkSource, GObject, Gio

from os import path
import subprocess

APP_NAME = "eidete"

# We can just patch this in for now for testing. It'd be a bit nicer to
# have it generate a .desktop file for this.
LAUNCHER_XML="""\
<?xml version="1.0" encoding="UTF-8"?>
<description>
  <name>Screencast</name>
  <description>Record a screencast</description>
  <icon name="gnome-mplayer"/>
  <category>Graphics</category>
  <command>%s</command>
</description>
"""

