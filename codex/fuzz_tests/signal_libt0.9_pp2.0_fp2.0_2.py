import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#Version (only used for development purposes)
VERSION = '2017.06.12.0'

#Folders
if os.path.exists('/opt/orangecash') == False:
	DIR = os.path.join(os.path.expanduser('~'), '.local', 'share', 'orangecash')
else:
	DIR = '/opt/orangecash'

#Standard includes
import time
import os

#PyInstaller includes
if hasattr(sys, '_MEIPASS'):
	os.chdir(sys._MEIPASS)
	DIR = sys._MEIPASS

#Gtk includes
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from gi.repository import GdkPixbuf

#Debug
DEBUG = False

#Configuration
CONFIG = os.path.join(DIR, 'config.ini')

#Check that the directory exists
if
