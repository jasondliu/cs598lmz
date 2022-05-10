import ctypes
import ctypes.util
import threading
import sqlite3
import os
import subprocess
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Globals

# Global application configuration object
# This object is created once, used for static configuration
# and destroyed once when the application terminates
g_config = None

# Global main window object
# This object is created once, used for the lifetime of the application
# and destroyed once when the application terminates
g_window = None

# Global logger object
# This object is created once, used for the lifetime of the application
# and destroyed once when the application terminates
g_logger = None

# TODO: Make this configurable
# Global application name
g_appName = "PhotoFiler"

# Global application version string
g_versionString = "1.0.0"

# Global application build date
g_buildDate = "27 Mar 2018"

# Ensure that the application name is used in Window title
g_windowTitle = "{} - v{}".format(g_appName, g_versionString)

# TODO: Make this configurable
# Global SQLite database filename
