import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os, sys
import argparse
import logging

from gi.repository import GLib, GObject, Gdk, Gtk, Pango
GObject.threads_init()

from prymatex.utils import guess_bundle, osextra
from prymatex.core import config
from prymatex.core.settings import configurables
from prymatex.core.settings import PrymatexConfigurable
from prymatex.core.logger import setup_logger

from prymatex.core import PrymatexComponent
from prymatex.core.plugin.pluginmanager import PMXPluginManager
from prymatex.core.plugin.foldermanager import PMXBundleFolderManager
from prymatex.core.plugin.themesmanager import PMXThemesManager
from prymatex.gui.dialogs.preferences import PreferencesDialog
from prymatex.gui.dialogs.about import AboutDialog
from prymatex.gui
