import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys

VLC_LIB_PATH = ctypes.util.find_library("vlc")
if not VLC_LIB_PATH:
    raise Exception("Can't find VLC shared library")

libvlc = ctypes.CDLL(VLC_LIB_PATH)

# callback function to send encrypted key to stream cipher
def on_libvlc_media_player_playing(data, *args, **kwargs):
    player = data
    libvlc.libvlc_audio_set_callbacks(player, None, None, None, None, None, ctypes.c_void_p(player.stream_cipher))

class VlcPlayer(object):
    def __init__(self):
        self.instance = libvlc.libvlc_new()
        self.player = libvlc.libvlc_media_player_new(self.instance)

    def toggle_pause(self):
        libvlc.libvlc_media_player_pause(self.player)

    def set_playing(self, playing):
        if
