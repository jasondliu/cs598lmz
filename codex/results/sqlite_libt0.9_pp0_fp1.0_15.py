import ctypes
import ctypes.util
import threading
import sqlite3
import locale
import os
import shutil

import gtk
import gobject

from gettext import gettext as _

import eyefi
from eyefi.ThumbnailHistogram import ThumbnailHistogram
from eyefi.ThumbnailHistogram import ThumbnailHistogram
from eyefi._constants import *
from eyefi.Config import Config
from eyefi.Config import _Config
from eyefi.DbusService import DbusService
from eyefi.SingleShot import SingleShot
from eyefi.AppletSignals import AppletSignals
from eyefi.CfProperties import CfProperties
from eyefi.CardManager import CardManager
from eyefi.TransferQueue import TransferQueue


class Applet(object):
    '''Main applet class. Most of the work is done in the background, on
    dbus, so the applet itself does not really do much. Most of the dbus
    activity is controlled by the CardManager.
    '''
    def __init__(self, applet, iid):
        self.applet = applet

