import ctypes
import ctypes.util
import threading
import sqlite3
import time

class Wificard:
    """
    Wifi card object
    """
    def __init__(self, name, mac):
        self.name = name
        self.mac = mac
        self.bssid = None
        self.channel = None
        self.essid = None
        self.signal = None
        self.quality = None
        self.noise = None
        self.bitrates = None
        self.encryption = None

    def get_name(self):
        return self.name

    def get_mac(self):
        return self.mac

    def get_bssid(self):
        return self.bssid

    def get_channel(self):
        return self.channel

    def get_essid(self):
        return self.essid

    def get_signal(self):
        return self.signal

    def get_quality(self):
        return self.quality

    def get_noise(self):
        return self.noise

    def get_bitrates(self):
        return
