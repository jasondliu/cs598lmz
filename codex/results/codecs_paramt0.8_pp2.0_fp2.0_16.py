import codecs
codecs.register_error('strict', codecs.ignore_errors)

try:
    import pygtk
    pygtk.require("2.0")
except:
    pass

try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)

try:
    import gconf
except:
    # fallback to gsettings
    pass

import os
import platform
try:
  import configobj
except ImportError:
  import warnings
  warnings.warn("configobj is not installed, we won't be able to load or save preferences")


class SystemConfiguration(object):
    """
    Pulls in configuration settings from system-wide configuration files.
    This is a base class which knows nothing about the location of the
    system-wide configuration files, and is subsequently not useful.
    """

    def __init__(self):
        # cache for the system configuration
        self._systemConfig = None

        # where the system-wide config files are found
        self.systemConfigDir = ""

        # where we installed our own configuration files
        self.configDir
