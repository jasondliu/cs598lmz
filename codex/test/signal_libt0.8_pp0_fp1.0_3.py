import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import sys
import gettext
import locale

# autostart applet
import autostart
autostart.autostart()

# i18n
current_locale, encoding = locale.getdefaultlocale()
locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
domain = 'mate-applets'
gettext.bindtextdomain(domain, locale_path)
gettext.textdomain(domain)
_ = gettext.gettext

# Applet name
APP_NAME = _("Sensors")

# Applet description
APP_DESC = _("A System Monitor applet")

# Window class
WINDOW_CLASS = "MateSensorsApplet"

# List of available sensors
