import ctypes
import ctypes.util
import threading
import sqlite3
import json
import os
import time
import re
import sys
import urllib
import urllib2
import cookielib
import datetime
import subprocess

import requests
import pygst
pygst.require("0.10")
import gst

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcgui
import xbmcvfs

__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__cwd__ = __addon__.getAddonInfo('path')
__version__ = __addon__.getAddonInfo('version')
__language__ = __addon__.getLocalizedString

__profile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__resource__ = xbmc.translatePath(os.path.join(__cwd__, 'resources', 'lib'))
__temp__ =
