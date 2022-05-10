import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import time
import gtk
import gobject
import pango
import webkit
import json
import subprocess
import threading
import urllib
import urllib2
import re
import hashlib
import base64
import tempfile
import shutil
import socket
import ssl
import gettext
import locale
import dbus
import dbus.service
import dbus.mainloop.glib
import ConfigParser

from dbus.mainloop.glib import DBusGMainLoop
from dbus.exceptions import DBusException
from gtk import gdk

# i18n
gettext.install("webaccounts-google-extension", "/usr/share/locale")

# i18n for menu item
menuName = _("Google")
menuGenericName = _("Web Account")

# i18n for NSS
nss = _("NSS")

# i18n for PKCS#11
pkcs11 = _("PKCS#
