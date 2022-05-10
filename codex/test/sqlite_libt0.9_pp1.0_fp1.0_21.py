import ctypes
import ctypes.util
import threading
import sqlite3
import os
import signal

class StatusLine:
    def __init__(self, oh):
        self.oh = oh
        self.song = '[no song playing]'
        self.artist = '[no song playing]'
        self.album = '[no song playing]'
        self.status = '[not playing]'
        self.status2 = '[not playing]'
        self.file = ''
        self.timestamp = int(time.time())
        self.playing = False
        self.update_subscription = self.oh.subscribe('/player/status', self.status_handler)
        self.subscription = self.oh.subscribe('/player/song', self.song_handler)
        self.stopped_subscription = self.oh.subscribe('/player/stopped', self.stop_handler)
        self.subscription.subscribe()
        self.update_subscription.subscribe()
        self.stopped_subscription.subscribe()

    def stop_handler(self):
        self.status = 'Stopped.'
