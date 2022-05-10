import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
sqlite3.connect('test.db')

from . import vlc


# This is a global variable
# If there is a change in the state of the media, then the callback function
# will be called.
vlc_event_manager = None


class VLCPlayer(object):
    """
    This class is used to play the media player.
    """
    def __init__(self, instance, player, global_callback, instance_callback):
        self._instance = instance
        self._player = player
        self._global_callback = global_callback
        self._instance_callback = instance_callback

    def play(self):
        """
        Play the media player.
        """
        return vlc.libvlc_media_player_play(self._player)

    def stop(self):
        """
        Stop the media player.
        """
        return vlc.libvlc_media_player_stop(self._player)

    def pause(self):
        """
        Pause the media player.
        """
        return vlc.libvlc_media
