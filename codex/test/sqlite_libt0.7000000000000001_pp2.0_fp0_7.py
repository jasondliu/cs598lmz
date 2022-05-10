import ctypes
import ctypes.util
import threading
import sqlite3
import os

from optparse import OptionParser
from xml.dom import minidom

from dbus import SystemBus, Interface, SessionBus, DBusException

from player import Player
from list import List

class DBusService(object):
    def __init__(self):
        self.dbus_name = 'org.mpris.MediaPlayer2.core'
        self.dbus_path = '/org/mpris/MediaPlayer2'
        self.dbus_interface = 'org.mpris.MediaPlayer2'
        self.dbus_player_interface = 'org.mpris.MediaPlayer2.Player'
        self.dbus_tracklist_interface = 'org.mpris.MediaPlayer2.TrackList'
        self.dbus_properties_interface = 'org.freedesktop.DBus.Properties'
        self.dbus_objects_interface = 'org.freedesktop.DBus.ObjectManager'
        self.dbus_peer_interface = 'org.freedesktop.DBus.Peer'
       
