import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')

class Playlist(object):
    '''
    A Playlist is a list of Media objects.
    '''

    def __init__(self, list_of_media_objects=None):
        if list_of_media_objects:
            self.playlist = list_of_media_objects[:]
        else:
            self.playlist = []
        self.current = 0
        self.playing = False
        self.shuffle = False
        self.repeat = False

    def __getitem__(self, index):
        return self.playlist[index]

    def __len__(self):
        return len(self.playlist)

    def add(self, media):
        self.playlist.append(media)

    def remove(self, media):
        self.playlist.remove(media)

    def clear(self):
        self.playlist = []
        self.current = 0

    def next(self):
        self.current += 1
        if self.current >= len(self.playlist):
            self.
