import ctypes
import ctypes.util
import threading
import sqlite3
import sqlite3.dbapi2 as lite
import os
import time

from gi.repository import Gtk, Gdk, GObject, GLib, Notify

def _(message) :
	return message

try :
	import gettext
	if os.path.exists("/usr/share/locale/") :
		gettext.setlocale(gettext.LC_ALL, "")
		gettext.bindtextdomain("ccsm", "/usr/share/locale/")
		gettext.textdomain("ccsm")
	else :
		gettext.bindtextdomain("ccsm", "./po")
		gettext.textdomain("ccsm")

except Exception, exception :
	print exception

#~ Locale = {
	#~ "Chinese": _("Chinese"),
	#~ "English": _("English"),
	#~ "French": _("French"),
	#~ "German": _("German"),
	#~ "Italian": _("Italian"),
	#~ "Russian": _("Russian"),

